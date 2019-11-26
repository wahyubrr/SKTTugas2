import zerorpc

peer1 = zerorpc.Client()
peer1.connect("tcp://127.0.0.1:4141")
peer2 = zerorpc.Client()
peer2.connect("tcp://127.0.0.1:4242")
peer3 = zerorpc.Client()
peer3.connect("tcp://127.0.0.1:4343")

class HelloRPC(object):
	def hello(self, name):
		return "Hello, %s" % name

	def create(self, data):
		return data

	def read(self, data):
		return data

	def update(self, data):
		return data

	def delete(self, data):
		return data

server = zerorpc.Server(HelloRPC())
server.bind("tcp://0.0.0.0:4040")
server.run()