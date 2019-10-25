import requests
import netifaces
import pprint

from win10toast import ToastNotifier

BASE_URL = 'https://192.168.0.1'

gateways = netifaces.gateways()
BASE_URL = gateways['default'][netifaces.AF_INET][0]
pprint.pprint(gateways)

obj_login = {
    'UserName' : 'Admin',
    'PassWord' : 'admin',
}

r = requests.post(url=BASE_URL, data=obj_login)
