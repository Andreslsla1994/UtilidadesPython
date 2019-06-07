import zeep
import json
import datetime
import decimal
import logging

class Client:

    def __init__(self):
        self.wsdl = 'http://localhost/WS_VTCOnline/?wsdl'
        self.client = zeep.Client(wsdl=self.wsdl)

    def BuscarVoucher(self):
        response = self.client.service.BuscarVoucher('20190530', '20190606', '79500481', 'TODOS', 'andresL','andresL')
        return self.responseToJson(response)
    def ObtenerAgencias(self, _user):
        response = self.client.service.ObtenerAgencias(_user)
        print(response)
        return self.responseToJson(response)
    def ObtenerUsuarios(self, _user):
        response = self.client.service.ObtenerUsuarios(_user)
        return self.responseToJson(response)


    def responseToJson(self, response):
        _key = list(response._value_1._value_1[0].keys())[0]
        _jsonResult = []
        for item in response._value_1._value_1:
            _jsonResult.append(item[_key])
        input_dict = zeep.helpers.serialize_object(_jsonResult)
        _json = json.loads(json.dumps(input_dict, default=myconverter))
        return _json


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return o.__str__()


 