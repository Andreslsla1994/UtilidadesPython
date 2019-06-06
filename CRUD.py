import pyodbc
import json
import datetime

class Crud:

    def __init__(self, _stringConection ):
        self._stringConection = _stringConection

    def select_to_Json(self, _query):
        conn = pyodbc.connect(self._stringConection)
        cursor = conn.cursor()
        query = (_query)
        cursor.execute(query)
        items = []
        columns = cursor.description
        result = [{columns[index][0]: column for index, column in enumerate(value)} for value in cursor.fetchall()]
        conn.close()
        return json.dumps(result, default=myconverter)

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
