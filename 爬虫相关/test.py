import requests


url = "http://www.baidu.com/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}
proxie = {'https': '117.88.176.23:3000'}

res = requests.get(url, headers=header, proxies=proxie)
print(res.content.decode("utf-8"))