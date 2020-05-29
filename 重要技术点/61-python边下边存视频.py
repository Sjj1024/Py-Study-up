import requests
from tqdm import tqdm

url = "http://w3.huawei.com/servicedesk/itservice/casemanage/download?id=7c1691c704884267bd3f05001197b496&dlType=attachment"

r = requests.get(url, stream=True)

with open('receive.mp4', "wb") as mp4:
    for chunk in tqdm(r.iter_content(chunk_size=1024)):
        # print("下载中......")
        if chunk:
            mp4.write(chunk)

print("下载结束")
