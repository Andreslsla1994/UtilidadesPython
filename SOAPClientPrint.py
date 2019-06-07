import zeep
import json
import datetime
import decimal
from flask import Flask, request, jsonify, make_response

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return o.__str__()


wsdl = 'http://localhost/WS_VTCOnline/?wsdl'
client = zeep.Client(wsdl=wsdl)
#response = client.service.BuscarVoucher('20190530', '20190606', '79500481', 'TODOS', 'andresL','andresL')
response = client.service.ObtenerUsuarios('andresL')
_key = list(response._value_1._value_1[0].keys())[0]
_jsonResult = []
for item in response._value_1._value_1:
    _jsonResult.append(item[_key])

print(_jsonResult)
input_dict = zeep.helpers.serialize_object(_jsonResult)
_json = json.loads(json.dumps(input_dict, default=myconverter))
#_json = json.loads(json.dumps(response._value_1._value_1, default=myconverter))
#_json = json.dumps(response._value_1, default=str)
print(_json)



# import urllib
# import json
# import datetime
# from sqlalchemy import create_engine
# from Constantes import stringConexion
# from sqlalchemy.orm import Session
# import decimal


# def myconverter(o):
#     if isinstance(o, datetime.datetime):
#         return o.__str__()
#     if isinstance(o, decimal.Decimal):
#         return o.__str__()
# params = urllib.parse.quote_plus(stringConexion)
# engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
# engine.connect()


# result = engine.execute('select top 10 * from CashVTCOnLine..CCCF_Detalle_Electronico (nolock)')

# _json =  json.dumps([dict(r) for r in result], default=myconverter)
# result.close()
# print(_json)
