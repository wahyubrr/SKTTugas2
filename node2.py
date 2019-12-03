import zerorpc
import mysql.connector
import time
import random
import multiprocessing

# setup untuk database masing2
db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer2"
)
time.sleep(5)
print("running...")

peer1 = zerorpc.Client()
peer1.connect("tcp://127.0.0.1:4041")
peer2 = zerorpc.Client()
peer2.connect("tcp://127.0.0.1:4042")
peer3 = zerorpc.Client()
peer3.connect("tcp://127.0.0.1:4043")

# variable yang isinya beda2 tiap peer
peerID = 2
isLeader = False
print("Leader stauts: ", isLeader)

def count_and_broadcast():
	t = random.randint(1,6)
	print("counter: ", t)
	time.sleep(t)
	# setelah ini, kirim broadcast ke semua peer
	if peer1.accept_leader():
		isLeader = True
		print(peerID, " is the leader: ", isLeader)
	if peer3.accept_leader():
		isLeader = True
		print(peerID, " is the leader: ", isLeader)

def broadcast():
	while True:
		if isLeader:
			peer1.acknowledge_leader()
			peer3.acknowledge_leader()
		time.sleep(0.5)
		print("run")

process = multiprocessing.Process(target = broadcast)
process.start()

class Peer(object):
	def __init__(self):
		process = multiprocessing.Process(target = count_and_broadcast)
		process.start()

	def acknowledge_leader(self):
		# untuk slave mengetahui jika masih terdapat leader
		process.terminate()
		print("reset process")
		process = multiprocessing.Process(target = count_and_broadcast)
		process.start()

	def accept_leader(self):
		# untuk slave mengiyakan sebuah leader
		return True

	def discover_leader(self):
		if peer1.isLeader():
			return str(4041)
		elif peer3.isLeader():
			return str(4043)

	def isLeader(self):
		return isLeader

	def create(self, data):
		cursor = db.cursor()
		sql = "INSERT INTO mahasiswa (name, nim) VALUES (%s, %s)"
		val = (data['nama'], data['nim'])
		cursor.execute(sql, val)
		db.commit()
		if isLeader == 1:
			# perintah untuk slave untuk mengupdate databasenya masing2
			peer1.create(data)
			peer3.create(data)
		return ("Database %s telah diupdate", peerID)

	def read(self):
		cursor = db.cursor()
		sql = "SELECT * FROM mahasiswa"
		cursor.execute(sql)
		results = cursor.fetchall()
		if isLeader == 1:
			# perintah untuk slave untuk mengupdate databasenya masing2
			peer1.read()
			peer3.read()
		return results

	def update(self, dataold, data):
		cursor = db.cursor()
		sql = "UPDATE mahasiswa SET name=%s, nim=%s WHERE name=%s"
		val = (data['nama'], data['nim'], dataold['nama'])
		cursor.execute(sql, val)
		db.commit()
		if isLeader == 1:
			# perintah untuk slave untuk mengupdate databasenya masing2
			peer1.update(dataold, data)
			peer3.update(dataold, data)

	def delete(self, data):
		cursor = db.cursor()
		sql = "DELETE FROM mahasiswa WHERE name=%s AND nim=%s"
		val = (data['nama'], data['nim'])
		cursor.execute(sql, val)
		if isLeader == 1:
			# perintah untuk slave untuk mengupdate databasenya masing2
			peer1.delete(data)
			peer3.delete(data)

db.commit()

server = zerorpc.Server(Peer())
server.bind("tcp://0.0.0.0:4042")
server.run()