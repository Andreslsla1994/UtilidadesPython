__all__ = ["RestApi"]
__version__ = "1.0"

import logging
import datetime
import jwt
import json
from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
from Constantes import stringConexion
from CRUD import Crud
from functools import wraps
from pythonFirebase import FirebaseUI

#Configuraciones
app = Flask(__name__)
CORS(app, support_credentials=True)
app.config['SSECRET_KEY'] = 'thissecretkey'



def token_required(f):
    @wraps(f)
    def decorate(*args, **kwargs):
        token = None
        #logging.warning(request.headers)
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing'}), 401
        try:
            data = jwt.decode(token, app.config['SSECRET_KEY'])
        except:
            return jsonify({'message': 'Token is invalid'}), 401
        return f(*args, **kwargs)
    return decorate

#Catalogos
@app.route('/aerolineas', methods=['GET'])
def getAerolineas():
    _command = Crud(stringConexion)
    _query = ("select '0' as id_empresa,'SELECCIONAR' as nombre,'' as nombre_corto union all "
                   "select * from CashVTCOnLine..View_ListaDeAerolineas with (nolock) "
                   "order by nombre_corto")
    return _command.select_to_Json(_query)
@app.route('/tipoCredito', methods=['GET'])
def getTipoCredito():
    _command = Crud(stringConexion)
    _query = ("select * from CashManagement..VTC_TipoCredito with (nolock) order by 1")
    return _command.select_to_Json(_query)
@app.route('/agencias', methods=['POST'])
def getAgencias():
    _command = Crud(stringConexion)
    _user = request.args.get('user')
    logging.warning(_user)
    
    _query = ("SELECT [id_agencia] "
                   "FROM [EasySeguridad]..[Usuarios] with (nolock) "
                   "WHERE [NombreCorto] = '"+_user+"' ")
    result_set = _command.select(_query)
    _idAgencia = ""
    for row in result_set:
        _idAgencia = row[0]

    _query = ("SELECT DISTINCT [Codigo] + ' - ' + rtrim(Nombre) AS [Nombre], [Codigo], TipoSignature  "
             "FROM [CashManagement]..[CM_Agencias_Viaje] with (nolock) "
             "WHERE [Codigo] LIKE '" + _idAgencia + "' ")
    return _command.select_to_Json(_query)
@app.route('/menu', methods=['GET'])
def getMenu():
    _command = Crud(stringConexion)
    _user = request.args.get('user')
    logging.warning(_user)
    _app = 'IAA'
    _query = ("select t.Modulo, "
                 "CONCAT('/Mantenimiento/', REPLACE(t.Descripcion, ' ', '')) as Path, "
                 "t.Descripcion, t.Indice_Transaccion as Indice " 
                   "  from easyseguridad..atribuciones a (nolock)"
                    "  inner join EasySeguridad..Transacciones t (nolock)"
                    " on a.Transaccion=t.Transaccion where a.NombreCorto='"+_user+"' and "
                   "t.Aplicacion = '"+_app+"' order by t.Modulo asc"
             )
    return _command.select_to_Json(_query)
@app.route('/signature', methods=['POST'])
@token_required
def getSignature():
    _user = request.args.get('user')
    logging.warning(_user)
    _command = Crud(stringConexion)
    _query = ("select * from CashVTCOnline..View_SolicitudUsuariosTarjetas where CodigoUsuario = '"+_user+"'")
    return _command.select_to_Json(_query)



#Consultas
@app.route('/voucherHeaders', methods=['POST'])
@token_required
def voucherHeaders():
    _command = Crud(stringConexion)
    _query = ("select REPLACE(COLUMN_NAME,'_',' ') as COLUMN_NAME from INFORMATION_SCHEMA.COLUMNS where TABLE_NAME='CCCF_Detalle_Electronico_old_DataP'")
    return _command.select_to_Json(_query)
@app.route('/voucher', methods=['POST'])
@token_required
def voucher():
    _command = Crud(stringConexion)
    _query = ("select top 50 * from CashVTCOnLine..CCCF_Detalle_Electronico_old_DataP (nolock)")
    return _command.select_to_Json(_query)


#Login
@app.route('/login', methods=['GET'])
def login():
    try:
        _auth = request.authorization
        #_authDB = FirebaseUI.getData()
        #_data = json.loads(_authDB.data) 
        _data = {
            "andresL": {
                "Pass": "a",
                "User": "andresL"
            },
            "b": {
                "Pass": "b",
                "User": "b"
                }
        }
        logging.warning(_data)
        _dataUser = _data[_auth.username]
        if _auth and _auth.password == _dataUser["Pass"]:
            return jwt.encode({'user': _auth.username, 'exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=30) },app.config['SSECRET_KEY'])
        return make_response('Could not verify!', 401, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) 
    except Exception as e:
        if hasattr(e, 'message'):
            logging.error('Failed : '+ e.message)
        else:
            logging.error('Failed : '+ str(e))
        return make_response('Something went wrong!', 403, {'WWW-Authenticate' : 'Basic realm="Login Required"'}) 

        
@app.route('/token', methods=['GET'])
@token_required
def token():
    return 'Hola mundo'
@app.route('/fire', methods=['GET'])
def fire():
    return FirebaseUI.getData()

if __name__ == '__main__':
    app.debug=True
    app.run()