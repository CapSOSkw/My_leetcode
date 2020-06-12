import json
import requests
from ast import literal_eval

veid = '1158935'
api_key = 'private_cuWWdncwMvXnFnWGCkRcAUof'

def get_vps_info():
    url = "https://api.64clouds.com/v1/getServiceInfo?veid=1158935&api_key=private_cuWWdncwMvXnFnWGCkRcAUof"
    response = requests.get(url)

    print(response.text)


def test():
    url = 'router.asus.com'
