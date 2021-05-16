import time
import requests
from pprint import pprint


class SrakOwerFlowSimpleClient:
    
    def get_question(self,fromdate, todate, tag):
        parametrs = {
            'site' : 'stackoverflow',
            'fromdate' : fromdate,
            'todate' : todate,
            'tagged' : tag,
            'sort' : 'votes',
            'page' : 0,
            'pagesize' : 100
        }
        url = 'https://api.stackexchange.com/2.2/questions'
        has_more = True
        items = []
        while (has_more is True):
            parametrs['page'] += 1
            req = requests.get(url, params=parametrs)
            status_code = req.status_code
            if status_code == 200:
                has_more = req.json()['has_more']
                items += req.json()['items']
            else:
                print(f'Error {status_code }')    
        return items

    def get_two_day_last_question(self, tag):
       # two days:
        quant = 172800 
        time_line = int(time.time())
        return self.get_question(time_line - quant, time_line, tag)


if __name__ == '__main__':
    client = SrakOwerFlowSimpleClient()
    request = client.get_two_day_last_question('python')
    out = [line['title'] for line in request]
    pprint(out)
