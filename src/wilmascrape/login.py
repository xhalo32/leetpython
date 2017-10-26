import requests

url = 'http://wilma.espoo.fi'
session = requests.session()

r = session.post(url)#, data=login_data)
print r.text
