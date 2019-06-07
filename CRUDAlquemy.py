import urllib
import json
import datetime
from sqlalchemy import create_engine
from Constantes import stringConexion
from sqlalchemy.orm import Session
import decimal

class CrudAlchemy:

    def __init__(self, _stringConection ):
        self._stringConection = _stringConection
        params = urllib.parse.quote_plus(stringConexion)
        self.engine = create_engine("mssql+pyodbc:///?odbc_connect={}".format(params))
        

    def select_to_Json(self, _query):
        self.engine.connect()
        result = self.engine.execute(_query)
        _json =  json.dumps([dict(r) for r in result], default=myconverter)
        result.close()
        return _json


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(o, decimal.Decimal):
        return str(round(o, 2))
        #return o.__str__()
