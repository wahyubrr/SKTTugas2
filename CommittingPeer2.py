import zerorpc
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer2"
)

class CommittingPeer2(object):
	def create(self, data):
		cursor = db.cursor()
		sql = "INSERT INTO mahasiswa (name, nim) VALUES (%s, %s)"
		val = (data['nama'], data['nim'])
		cursor.execute(sql, val)
		db.commit()
		return "Database2 telah diupdate"

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

server = zerorpc.Server(CommittingPeer2())
server.bind("tcp://0.0.0.0:4242")
server.run()