from urllib.parse import urlencode
import requests
original_url = 'https://www.autohome.com.cn/ashx/AjaxIndexHotCarByDsj.ashx?'
requests_headers = {
    'Referer':'https://www.autohome.com.cn/beijing/',
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'X-Requested-With':'XMLHttpRequest',
}
def get_one(cityid):
    p = {
        'cityid':cityid
    }
    compelete_url=original_url+urlencode(p)
    try:
        response=requests.get(url=compelete_url,params=requests_headers)
        if response.status_code==200:
            return response.json()
    except requests.ConnectionError as e:
        print('Error',e.args)

def parse(json):
    if json:
        item=json[0].get('Name')
        print(item)

def parse_three(json):
    if json:
        for i in json:
            for b in i.get('SeriesList'):
                item_list = b.get('Name')
                item_list2 = b.get('Id')

if __name__=='__main__':
    jo = get_one(110100)
    parse(jo)