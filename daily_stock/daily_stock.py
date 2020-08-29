#encoding:UTF-8

import requests
import json
from sys import argv

URL = "https://www.wind.com.cn/NewSite/handler/IndexHandler.ashx?v=0.02208392134801951"
page = requests.get(URL)

data_dicts = json.dumps(
    json.loads(page.text.encode('utf-8').decode('utf-8')), 
    indent=4, 
    ensure_ascii=False,
    separators=(',', ':'),
    sort_keys=True)
print(data_dicts)

DESTINATION = argv[1]
jsonData = json.loads(page.text.encode('utf-8').decode('utf-8'))

desc = jsonData[0]['Name'] + ' 收：' + jsonData[0]['Price'] + ' 涨跌：' + jsonData[0]['ChangeRate'] + "\n\r\n\r" + jsonData[1]['Name'] + ' 收：' + jsonData[1]['Price'] + ' 涨跌：' + jsonData[1]['ChangeRate']
params = {'text':'每日财经数据','desp':desc}
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"}
requests.get(DESTINATION, params = params, headers = headers)