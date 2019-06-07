import pyodbc
import json
import datetime
import logging

class Crud:

    def __init__(self, _stringConection ):
        self._stringConection = _stringConection

    def select_to_Json(self, _query):
        conn = pyodbc.connect(self._stringConection)
        cursor = conn.cursor()
        query = (_query)
        cursor.execute(query)
        row_headers=[x[0] for x in cursor.description]
        rv = cursor.fetchall()
        logging.warning(rv)
        json_data=[]
        for result in rv:
            json_data.append(dict(zip(row_headers,result)))
        conn.close()
        _json = json.dumps(json_data, default=myconverter)
        
        return _json

    def select(self, _query):
        conn = pyodbc.connect(self._stringConection)
        cursor = conn.cursor()
        query = (_query)
        cursor.execute(query)
        result_set = cursor.fetchall()
        conn.close()
        return result_set

def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()
    if isinstance(0, float):
        return o.__str__()
