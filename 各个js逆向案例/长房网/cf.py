import execjs

node = execjs.get()
ctx = node.compile(open('changfang.js', encoding='utf-8').read())
funNname = 'getPwd("{0}")'.format('123456')
pwd = ctx.eval(funNname)
print(pwd)