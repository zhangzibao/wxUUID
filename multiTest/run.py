import time
from threading import Thread

import requests
from configs.log_config import logger

host = "http://101.227.51.149:10011"


# host = "http://localhost:5888" # 本地
def request_uuid():
    url = f"{host}/getUUID"

    payload = {
        "WxData": "A1074e50ecfc6c9e",
        "WechatVersion": 0,
        "DeviceVersion": "string",
        "XmlData": "string"
    }
    headers = {
        'token': 'hello',
        'User-Agent': 'Apifox/1.0.0 (https://www.apifox.cn)',
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, json=payload)
    res_json = response.json()
    if res_json["success"]:
        logger.debug(res_json)

    return res_json["success"]


def thread_run():
    for _ in range(10000):
        if not request_uuid():
            break
        time.sleep(1)


for _ in range(100):
    Thread(target=thread_run, args=()).start()
