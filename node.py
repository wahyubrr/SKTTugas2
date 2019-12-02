import zerorpc
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer1"
)

peer1 = zerorpc.Client()
peer1.connect("tcp://127.0.0.1:4141")
peer2 = zerorpc.Client()
peer2.connect("tcp://127.0.0.1:4242")
peer3 = zerorpc.Client()
peer3.connect("tcp://127.0.0.1:4343")
peer4 = zerorpc.Client()
peer4.connect("tcp://127.0.0.1:4344")
peer5 = zerorpc.Client()
peer5.connect("tcp://127.0.0.1:4345")

class LeaderPeer(object):
	def create(self, data):
		peer1.create(data)
		peer2.create(data)
		peer3.create(data)

	def read(self, index):
		if index == 1:
			data = peer1.read()
		if index == 2:
			data = peer2.read()
		if index == 3:
			data = peer3.read()

		return data

	def update(self, dataold, data):
		peer1.update(dataold, data)
		peer2.update(dataold, data)
		peer3.update(dataold, data)

	def delete(self, data):
		peer1.delete(data)
		peer2.delete(data)
		peer3.delete(data)

class SlavePeer(object):
	def create(self, data):
		cursor = db.cursor()
		sql = "INSERT INTO mahasiswa (name, nim) VALUES (%s, %s)"
		val = (data['nama'], data['nim'])
		cursor.execute(sql, val)
		db.commit()
		return "Database1 telah diupdate"

	def read(self):
		cursor = db.cursor()
		sql = "SELECT * FROM mahasiswa"
		cursor.execute(sql)

		results = cursor.fetchall()
		return results

	def update(self, dataold, data):
		cursor = db.cursor()
		sql = "UPDATE mahasiswa SET name=%s, nim=%s WHERE name=%s"
		val = (data['nama'], data['nim'], dataold['nama'])
		cursor.execute(sql, val)
		db.commit()

	def delete(self, data):
		cursor = db.cursor()
		sql = "DELETE FROM mahasiswa WHERE name=%s AND nim=%s"
		val = (data['nama'], data['nim'])
		cursor.execute(sql, val)

db.commit()

server = zerorpc.Server(LeaderPeer())
server.bind("tcp://0.0.0.0:4040")
server.run()