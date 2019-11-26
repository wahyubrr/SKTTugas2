import zerorpc

peer1 = zerorpc.Client()
peer1.connect("tcp://127.0.0.1:4141")
peer2 = zerorpc.Client()
peer2.connect("tcp://127.0.0.1:4242")
peer3 = zerorpc.Client()
peer3.connect("tcp://127.0.0.1:4343")

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

server = zerorpc.Server(LeaderPeer())
server.bind("tcp://0.0.0.0:4040")
server.run()