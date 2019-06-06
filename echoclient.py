from twisted.internet import reactor, protocol

class EchoClient(protocol.Protocol):
    def connectionMade(self):
        txt = input("Type something to test this out: ")
        self.transport.write(txt.encode())
        #self.transport.write("Hello, world".encode())

    def dataReceived(self, data):
        print(f"Server said: {data}")
        self.transport.loseConnection()

class EchoFactory(protocol.ClientFactory):
    def buildProtocol(self, addr):
        return EchoClient()

    def clientConnectionFailed(self, connector, reason):
        print("Connection failed.")
        reactor.stop()

    def clientConnectionLost(self, connector, reason):
        print("Connection lost")
        reactor.stop()

reactor.connectTCP("10.0.2.106", 9999, EchoFactory())
reactor.run()