import execjs
import requests
import re


url = 'http://login.shikee.com/getkey?v=8cbffe4962b93a0d79021dd70fecccb0'
resp = requests.get(url)
pat = re.compile('rsa_n = "(.*?)"',re.S)
rsa_n = re.findall(pat,resp.text)
node = execjs.get()
ctx = node.compile(open('shike.js', encoding='utf-8').read())
funcName = 'getPwd("{0}","{1}")'.format('123456',rsa_n)
pwd = ctx.eval(funcName)
print(pwd)
