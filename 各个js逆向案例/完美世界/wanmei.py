import requests
from lxml import etree
import execjs

url = "https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f"
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'
}
resp_text = requests.get(url=url,headers=headers).text
html = etree.HTML(resp_text)
key = html.xpath('//input[@id="e"]/@value')[0]
print(key)
node = execjs.get()
ctx = node.compile(open('wanmei.js', encoding='utf-8').read())
funcName = 'getPwd("{0}","{1}")'.format('123',key)
pwd = ctx.eval(funcName)
print(pwd)
