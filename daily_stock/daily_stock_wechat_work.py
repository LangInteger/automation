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

jsonData = json.loads(page.text.encode('utf-8').decode('utf-8'))

desc = jsonData[0]['Name'] + ' 收：' + jsonData[0]['Price'] + ' 涨跌：' + jsonData[0]['ChangeRate'] + "\n\r\n\r" \
     + jsonData[1]['Name'] + ' 收：' + jsonData[1]['Price'] + ' 涨跌：' + jsonData[1]['ChangeRate'] + "\n\r\n\r" \
     + jsonData[2]['Name'] + ' 收：' + jsonData[2]['Price'] + ' 涨跌：' + jsonData[2]['ChangeRate'] + "\n\r\n\r" \
     + jsonData[3]['Name'] + ' 收：' + jsonData[3]['Price'] + ' 涨跌：' + jsonData[3]['ChangeRate'] + "\n\r\n\r" \
     + jsonData[4]['Name'] + ' 收：' + jsonData[4]['Price'] + ' 涨跌：' + jsonData[4]['ChangeRate'] + "\n\r\n\r" \
     + jsonData[5]['Name'] + ' 收：' + jsonData[5]['Price'] + ' 涨跌：' + jsonData[5]['ChangeRate'] + "\n\r\n\r"
params = {'text':'每日财经数据','desp':desc}
repsonse = requests.post(argv[1], params)
print(response)