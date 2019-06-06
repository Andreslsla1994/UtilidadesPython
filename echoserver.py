from twisted.internet import protocol, reactor
from twisted.python import log

class Echo(protocol.Protocol):
    def dataReceived(self, data):
        resp = "006B600030002102103038010022C0004000300000000005835200862416575603070001375482443210068001D210420100000090000000303332363030313030373236303031202020202020202020200024303030303030303532313030303030303030303030303030"
        print(f"Data said: {data}")
        #self.transport.write(data)
        self.transport.write(resp.encode())

class EchoFactory(protocol.Factory):
    def buildProtocol(self, addr):
        return Echo()

reactor.listenTCP(6666, EchoFactory())
reactor.run()
