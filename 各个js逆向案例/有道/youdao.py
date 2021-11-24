import requests
import execjs
from hashlib import md5
import time
import random

word = input('输入你要翻译的词语:')
ts = str(int(time.time()*1000))
salt = ts+str(int(random.randint(0,9)))
node = execjs.get()
ctx = node.compile(open('./youdao.js',encoding='utf-8').read())
funcName = 'getSign("{0}")'.format(word)
sign = ctx.eval(funcName)
md = md5()
md_ = "fanyideskweb" + word + salt + "Y2FYu%TNSbMCxc3t2u^XT"
md.update(md_.encode())
sign = md.hexdigest()
headers = {
        'Accept':'application/json, text/javascript, */*; q=0.01',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'241',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'OUTFOX_SEARCH_USER_ID=-742091443@10.108.160.101; OUTFOX_SEARCH_USER_ID_NCOO=1219939988.1228168; fanyi-ad-id=118539; fanyi-ad-closed=1; JSESSIONID=aaaqzRoDxUEYjgi8tfAZx; ___rl__test__cookies=1635754580292',
        'Host':'fanyi.youdao.com',
        'Origin':'https://fanyi.youdao.com',
        'Pragma':'no-cache',
        'Referer':'https://fanyi.youdao.com/',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
        'X-Requested-With':'XMLHttpRequest',
}
data = {
        'i':word,
        'from':'AUTO',
        'to':'AUTO',
        'smartresult':'dict',
        'client':'fanyideskweb',
        'salt':salt,
        'sign':sign,
        'lts':ts,
        'bv':'c795a332c678d5063a1ee5eb15253848',
        'doctype':'json',
        'version':'2.1',
        'keyfrom':'fanyi.web',
        'action':'FY_BY_CLICKBUTTION',
}

url = 'https://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
resp = requests.post(url=url,headers=headers,data=data)
print(resp.json())

