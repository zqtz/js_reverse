import requests
import execjs
import time
ts = str(int(time.time()*1000))

url = 'https://store.steampowered.com/login/getrsakey/'
headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'45',
        'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie':'browserid=2600259388281572294; timezoneOffset=28800,0; _ga=GA1.2.1711822966.1635493545; _gid=GA1.2.1128289653.1635493545; steamCountry=CN%7C47c37b5fe4ed67f4719ab854070517f9; sessionid=971e0e4668c84154903d3096',
        'Host':'store.steampowered.com',
        'Origin':'https://store.steampowered.com',
        'Pragma':'no-cache',
        'Referer':'https://store.steampowered.com/login/?redir=&redir_ssl=1&snr=1_4_4__global-header',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-origin',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
}
form_data = {
    'donotcache':ts,
    'username':'investor_ai',
}
# print(form_data)
# resp = requests.post(url=url,headers=headers).json()
# exp = resp['publickey_exp']
# mod = resp['publickey_mod']
exp = '010001'
mod = 'c447c12d54794ffa7cef63bcc5c8ccc5daccdac17982edf27acbe2f5e14bba2447370c16bd5cc4452c1aded1933f22530bc94acfd9ba6296fa9b075fe21dfbf6fb1347e957867ff324e4c56310e9176926aaf6ce0b9b34f6ba0cf6fbebe75ffb9137d8df118f02d8b363c00209f47352957f2bc8565c43b96648526f36c82ea444a4be79794fced1f4cd7d64f409b970573ac08a7d6dc5a970e90ba6afc58c1d53862eaf2cd1570183129ccb6967aecabb3e8ac16a5581ef99e43b04e9ab137d5247dbea1193b690603c04f0bca212d6e6df76819260d1a6116b4730a9ab4be26bb8a97284a06f31e6fd58a0c0b43b509d4885eff393a9b7b42f7fc83e02c387'
# print(mod,exp)
node = execjs.get()
etx = node.compile(open('steam.js', encoding='utf-8').read())
funName = "getPwd('{}','{}','{}')".format('a19941030',mod,exp)
pwd = etx.eval(funName)
print(pwd)
