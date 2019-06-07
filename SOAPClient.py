import zeep
import json
import datetime
import decimal
class Client:

    def __init__(self):
        self.wsdl = 'http://localhost/WS_VTCOnline/?wsdl'

    def BuscarVoucher(self):
        client = zeep.Client(wsdl=self.wsdl)
        response = client.service.BuscarVoucher('20190530', '20190606', '79500481', 'TODOS', 'andresL','andresL')
        print(response)
        input_dict = zeep.helpers.serialize_object(response._value_1._value_1)
        _json = json.loads(json.dumps(input_dict, default=myconverter))
        return _json

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return o.__str__()


 