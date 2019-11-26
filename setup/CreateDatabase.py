import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

cursor = db.cursor()
cursor.execute("CREATE DATABASE committing_peer1")
cursor.execute("CREATE DATABASE committing_peer2")
cursor.execute("CREATE DATABASE committing_peer3")

print("Database berhasil dibuat!")