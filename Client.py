import zerorpc

client = zerorpc.Client()
client.connect("tcp://127.0.0.1:4040")
# print client.hello("RPC")

print("1. Create")
print("2. Read")
print("3. Update")
print("4. Destory")
select = input()

if select == 1:
	print("Create")
elif select == 2:
	print("Read")
elif select == 3:
	print("Update")
elif select == 4:
	print("Delete")
else:
	print("Pilihan tidak valid!")

# Create, Read, Update, Delete