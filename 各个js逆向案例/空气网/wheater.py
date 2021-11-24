import requests
import json

url = 'https://miao.baidu.com/abdr?'
headers = {
        'Accept':'*/*',
        'Accept-Encoding':'gzip, deflate, br',
        'Accept-Language':'zh-CN,zh-TW;q=0.9,zh;q=0.8,en-US;q=0.7,en;q=0.6',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Content-Length':'4020',
        'Content-Type':'text/plain;charset=UTF-8',
        'Cookie':'ab_jid=4e391acaf641253173cbe430e70e726161ec; ab_jid_BFESS=4e391acaf641253173cbe430e70e726161ec; BDUSS_BFESS=3dBMWg5LVBTZUd4Tk9sVk9lbGg5N2N6eG1QQUl1am9zdH5JUk1pM0FhakZrNU5oRVFBQUFBJCQAAAAAAAAAAAEAAAAQZ7vIs6S358bGwMvAssur0-MAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMUGbGHFBmxhM; BDSFRCVID_BFESS=zrLOJexroG01HYnHqj31bokt6gKK0gOTDYLEOwXPsp3LGJLVgK9uEG0Ptf8gjM--J8jwogKK3gOTH4AF_2uxOjjg8UtVJeC6EG0Ptf8g0M5; H_BDCLCKID_SF_BFESS=tbkD_C-MfIvDqTrP-trf5DCShUFsQpbRB2Q-XPoO3KtaOMTkybQ8DPuVhURJttbiWbRM2MbgylRp8P3y0bb2DUA1y4vpKMP8bmTxoUJ25DnJjlCzqfCWMR-ebPRiJ-b9Qg-J5lQ7tt5W8ncFbT7l5hKpbt-q0x-jLTnhVn0MBCK0hI0ljj82e5PVKgTa54cbb4o2WbCQKMJO8pcN2b5oQTOLybrXBnoBt26aWbv2JJ3vOIJTXpOUWfAkXpJvQnJjt2JxaqRC5hkBfq5jDh3Mb6ksM4FLexIO2jvy0hvctb3cShPmLfjrDRLbXU6BK5vPbNcZ0l8K3l02V-bIe-t2XjQhDNtDt60jfn3aQ5rtKRTffjrnhPF3hb8UXP6-hnjy3b4DaUT8WPj8hU5PhPRMj4-UyN3MWh3RymJ42-39LPO2hpRjyxv4bUn-5toxJpOJ5JbMBqCEHlFWj43vbURvDP-g3-AJ3x5dtjTO2bc_5KnlfMQ_bf--QfbQ0hOhqP-jBRIEoK0hJC-2bKvPKITD-tFO5eT22-usfR7C2hcHMPoosItlyhr_yb_qDPja2-nJJDviaKJjBMbUoqRHXnJi0btQDPvxBf7p5208Ll5TtUJMeCnTMxFVqfTbMlJyKMnitKv9-pP20lQrh459XP68bTkA5bjZKxtq3mkjbPbDfn028DKuDTtajj3QeaRabK6aKC5bL6rJabC3J4osXU6q2bDeQN0DBpcXWT6BoKjtabvMMR3oyT3JXp0vWtv4WbbvLT7johRTWqR4epkw5fonDh83bG7MafuLHmLOBt3O5hvvhn3O3MAMLfKmDloOW-TB5bbPLUQF5l8-sq0x0bOte-bQXH_E5bj2qRPqoC0h3D; BAIDUID_BFESS=DC4E873F793E88DDE65B010923710DB5:FG=1; ab_bid=b3a2a32e7c6748f9246f535fa1fa125f153b; ab_sr=1.0.1_ZDQ4MDhlZjhkZDcwMGExMTM2ZmZlNjQyMzAyY2MxZWY4MzEwZWNkMDE0NTUwOGM0Mjc4MzBkN2Q3NTQxYTIxMzQ5Njg2MWNmNGNhMDlhYjEwNTJmODlmMzdkNDM5YWZhNTZlZTU0YjhlNWM0YjRiYjkzOGM3NDYwODkwYWUxYTk1Y2IzNTlmYmNmYjViNWFlMWViOTQ3MDE2OWY1YmUxOQ==',
        'Host':'miao.baidu.com',
        'Origin':'https://m.zq12369.com',
        'Pragma':'no-cache',
        'Referer':'https://m.zq12369.com/',
        'sec-ch-ua':'"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile':'?0',
        'sec-ch-ua-platform':'"Windows"',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'cross-site',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
}
data = {'_o': 'https%3A%2F%2Fm.zq12369.com'}
resp = requests.post(url=url,headers=headers,data=json.dumps(data))
print(resp.text)




