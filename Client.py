import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4040")
# print client.hello("RPC")

while 1:
	print("1. Create")
	print("2. Read")
	print("3. Update")
	print("4. Destory")
	select = input()

	if select == "1":
		nama = input("Masukkan nama anda: ")
		nim = input("Masukkan nim anda: ")
		data = {'nama': nama, 'nim': nim}
		client.create(data)

	elif select == "2":
		datap1 = client.read(1)
		datap2 = client.read(2)
		datap3 = client.read(3)

		print("Data dari peer1")
		for data in datap1:
			print(data)

		print("Data dari peer2")
		for data in datap2:
			print(data)

		print("Data dari peer3")
		for data in datap3:
			print(data)

	elif select == "3":
		namaold = input("Masukkan nama anda yang ingin datanya diubah: ")
		nama = input("Masukkan nama anda yang baru: ")
		nim = input("Masukkan nim anda yang baru: ")
		dataold = {'nama': namaold}
		data = {'nama': nama, 'nim': nim}

		client.update(dataold, data)

	elif select == "4":
		nama = input("Masukkan nama anda: ")
		nim = input("Masukkan nim anda: ")
		data = {'nama': nama, 'nim': nim}
		client.delete(data)

	else:
		print("Pilihan tidak valid!")

	print("")

# Create, Read, Update, Delete