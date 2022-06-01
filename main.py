import math
import requests
import base64
import re


def str_convert(text: str):
    base64_ = base64.b64encode(text.encode("utf-8"))
    target_num = int(re.findall(r"[1-9]", str(base64_))[0])
    for i in re.findall(r"[1-9]", str(base64_))[1:]:
        target_num = target_num * int(i)
    return math.modf(math.log(int(re.sub(r"0", "", str(target_num)))))[0]


def generate_target():
    response = requests.get("https://v1.jinrishici.com/all.json", )
    return {
        "target": str_convert(response.json().get("content")),
        "shi": response.json()
    }


def select_food(foods: list):
    target = generate_target()
    return {
        "food": foods[int(math.modf(len(foods) * target["target"])[1])],
        "shi": target["shi"]["content"]
    }
