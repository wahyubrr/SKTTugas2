import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer1"
)
cursor = db.cursor()
sql = """CREATE TABLE mahasiswa (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  nim Varchar(255)
)
"""
cursor.execute(sql)

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer2"
)
cursor = db.cursor()
sql = """CREATE TABLE mahasiswa (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  nim Varchar(255)
)
"""
cursor.execute(sql)

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password",
  database="committing_peer3"
)
cursor = db.cursor()
sql = """CREATE TABLE mahasiswa (
  customer_id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  nim Varchar(255)
)
"""
cursor.execute(sql)

print("Tabel mahasiswa berhasil dibuat!")