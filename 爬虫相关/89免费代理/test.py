import requests
from lxml import etree

url = "http://www.89ip.cn/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"}

res = requests.get(url, headers=header)
xml_obj = etree.HTML(res.content.decode("utf-8"))
ip_source_list = xml_obj.xpath("/html/body//tr/td/text()")
good_ip_list = [i.strip() for i in ip_source_list]
print(good_ip_list)
print(len(good_ip_list))
