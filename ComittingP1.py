import zerorpc

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
server.bind("tcp://0.0.0.0:4141")
server.run()