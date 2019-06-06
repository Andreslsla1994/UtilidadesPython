import requests
from firebase import firebase


url = 'http://10.0.2.106/WS_VTCOnline/VTCOnline.asmx'
body = """<?xml version="1.0" encoding="UTF-8"?>
         <soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:tem="http://tempuri.org/">
           <soapenv:Header/>
           <soapenv:Body>
              <tem:ObtenerAerolineas/>
           </soapenv:Body>
        </soapenv:Envelope>"""
headers = {'content-type': 'text/xml'}

# Retrieve a single page and report the URL and contents
def get_account_info():
    response = requests.post(url,data=body,headers=headers)
    print(response.status_code)
    if response.status_code == 200:
        print(response.content)
    else:
        print('Error')

def consume_firebase():
    _firebase = firebase.FirebaseApplication('https://loginreact-f8c1d.firebaseio.com', None)
    result = _firebase.get('/estado', None)
    print(result)
    return result

consume_firebase()