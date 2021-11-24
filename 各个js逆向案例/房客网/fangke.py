import execjs

node = execjs.get()
ctx = node.compile(open('fanke.js', encoding='utf-8').read())
funcName = "md5('{0}')".format('123')
pwd = ctx.eval(funcName)
print(pwd)
