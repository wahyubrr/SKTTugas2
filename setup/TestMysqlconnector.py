import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="user",
  passwd="password"
)

if db.is_connected():
  print("Berhasil terhubung ke database")