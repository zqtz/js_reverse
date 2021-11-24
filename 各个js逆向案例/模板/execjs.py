import execjs
import requests

node = execjs.get()
ctx = node.compile(open('./....js',encoding='utf-8').read())
funcName = '({})'.format()
pwd = ctx.eval()
print(pwd)
