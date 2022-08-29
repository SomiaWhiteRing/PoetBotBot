import requests
import json
from func.getIp import get_host_ip

class weiboClient():

    def post(self, status, access_token):

        url = 'https://api.weibo.com/2/'
        api = 'statuses/update.json'
        ip = get_host_ip()
        data = {
            'status': status,
            'access_token': access_token,
            'visible': 1,
            'is_longtext': 1,
            'rip': ip
        }
        result = requests.post(url + api, data=data)
        print(result.text)
        return json.loads(result.text)
