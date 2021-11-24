import requests
import execjs
import re

url = 'https://sso.kongzhong.com/ajaxLogin?j=j&&type=1&service=https://passport.kongzhong.com/&username=15916142395&password=41401e2a6553d14f4caa04f41e80&vcode=ki93&toSave=0&_=1635578311083'
headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Cookie':'SSO-KGZQRT=E6687EA5E937FE73E930B66CC700B9F7; KZLBS=d08e6bcdc9f0cbe5; Hm_lvt_1287c2225a527abe3386233dd9316f99=1635563223,1635563315,1635564362,1635576606; Hm_lpvt_1287c2225a527abe3386233dd9316f99=1635576606; SSO-KGZLT=bb0c9aae-c3bf-4a22-ab17-6339f6ad684b; SSO-KGZIT=e04f7bc2-3ec5-49ee-b7ad-e0d74ebaa8b8',
        'Host':'sso.kongzhong.com',
        'Pragma':'no-cache',
        'Referer':'https://passport.kongzhong.com/',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'script',
        'Sec-Fetch-Mode':'no-cors',
        'Sec-Fetch-Site':'same-site',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
}
resp = requests.get(url,headers=headers)
pat = re.compile('"dc":"(.*?)"',re.S)
doc = re.findall(pat,resp.text)[0]
node = execjs.get()
ctx = node.compile(open('kongzhong.js', encoding='utf-8').read())
funcName = 'getPwd("{0}","{1}")'.format('123456',doc)
pwd = ctx.eval(funcName)
print(pwd)

