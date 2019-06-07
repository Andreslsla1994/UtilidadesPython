server = '10.0.2.56'
database = 'CashVTCOnline'
username = 'sa'
password = 'E@sysoft'
#driver = '{SQL Server}' # Driver you need to connect to the database
driver = '{ODBC Driver 17 for SQL Server}'
port = '1433'
client_id='1764119c-9efd-4784-a7a0-ab29f9ec045f'
client_secret='0NhgMOuSe6RDFJHLrRzyjhNTM0XomyVhgdWDHSDRPPs='

stringConexion = ('DRIVER='+driver+';PORT=port;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+password+
                      ';ColumnEncryption=Enabled;KeyStoreAuthentication=KeyVaultClientSecret;KeyStorePrincipalId='+client_id+';KeyStoreSecret='+client_secret)
