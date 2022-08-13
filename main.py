from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
from emoji import emojize
today = datetime.now()
start_date = "2018-09-07"
city = "松江区"
birthday = "11-06"
app_id = "wx98e8c8cabb4b1d51"
app_secret = "2b805f6c8c2e3271c16232cade770a4d"
city_data = "上海"
user_id = "ozFNU6Bp7BF2_nF2cyIBGWGa4DcI"
template_id = "fJN68unFFZ1vXlOy_3cQY4XKSHmBouiByHTjiwpO-To"
def get_weather_emoji():
  wea, temperature = get_weather()
  if wea == "多云":
    return "\U000026C5"
  elif wea == "小雨" or wea == "大雨" or wea == "中雨":
    return "\U0001F327"
  elif wea == "晴":
    return "\U0001F31E"
  elif wea == "阴":
    return "\U00002601"
  elif wea == "阵雨":
    return "\U0001F326)"
  elif wea == "雷阵雨":
    return "\U000026C8"
  else:
    return "\U0001F31A"
def get_weather():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['weather'], math.floor(weather['temp'])

def get_weather_other():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['wind'], math.floor(weather['pm25'])

def get_weather_other_1():
  url = "http://autodev.openspeech.cn/csp/api/v2.1/weather?openId=aiuicus&clientType=android&sign=android&city=" + city
  res = requests.get(url).json()
  weather = res['data']['list'][0]
  return weather['airQuality'], weather['humidity']

def get_count():
  delta = today - datetime.strptime(start_date, "%Y-%m-%d")
  return delta.days

def get_birthday():
  next = datetime.strptime(str(date.today().year) + "-" + birthday, "%Y-%m-%d")
  if next < datetime.now():
    next = next.replace(year=next.year + 1)
  return (next - today).days

def get_words():
  words = requests.get("https://api.shadiao.pro/chp")
  if words.status_code != 200:
    return get_words()
  return words.json()['data']['text']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)


client = WeChatClient(app_id, app_secret)

wm = WeChatMessage(client)
emoji = get_weather_emoji()
wea, temperature = get_weather()
wind, pm25 = get_weather_other()
airQuality, humidity = get_weather_other_1()
data = {"airQuality":{"value":airQuality,"color":get_random_color()},"humidity":{"value":humidity,"color":get_random_color()},"city_data":{"value":city_data,"color":get_random_color()},"weather":{"value":wea,"color":get_random_color()},"temperature":{"value":temperature,"color":get_random_color()},"wind":{"value":wind,"color":get_random_color()},"pm25":{"value":pm25,"color":get_random_color()},"love_days":{"value":get_count(),"color":get_random_color()},"birthday_left":{"value":get_birthday(),"color":get_random_color()},"words":{"value":get_words(), "color":get_random_color()}, "emoji":{"value":emoji}}
res = wm.send_template(user_id, template_id, data)
print(res)
