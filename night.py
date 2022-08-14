from datetime import date, datetime
import math
from wechatpy import WeChatClient
from wechatpy.client.api import WeChatMessage, WeChatTemplate
import requests
import os
import random
from emoji import emojize

app_id = "wx98e8c8cabb4b1d51"
app_secret = "2b805f6c8c2e3271c16232cade770a4d"
city_data = "上海"
user_id = "ozFNU6PNX1sG8WUIwX39XGHX3Ato"
template_id = "zHlwhURaIEcWUkhBz3JZeZBooS5FcI8kupbVXPvyXic"

def get_night():
  url = "http://api.tianapi.com/wanan/index?key=c8b2eba47b061235469c38e99ee3c856"
  res = requests.get(url).json()
  night = res['newslist'][0]
  
  return night['content']

def get_random_color():
  return "#%06x" % random.randint(0, 0xFFFFFF)

night_ = "天黑了该睡觉了"
night_1 = get_night()
night_2 = "晚安唔西迪西"
night_3 = "晚安玛卡巴卡"
night_4 = "晚安依古比古"
night_5 = "晚安小点点"
night_6 = "晚安叮叮车"
night_7 = "晚安飞飞鱼"
night_8 = "晚安袁宝"

emoji_ = "\U0001F319"
emoji_1 = "\U0001F33F"
emoji_2 = "\U0001F4AE"
emoji_3 = "\U0001F338"
emoji_4 = "\U0001F3F5"
emoji_5 = "\U0001F33A"
emoji_6 = "\U0001F340"
emoji_7 = "\U00002764"

client = WeChatClient(app_id, app_secret)

data = {"night_1":{"value":night_1,"color":get_random_color()},"night_":{"value":night_,"color":get_random_color()},"night_2":{"value":night_2,"color":get_random_color()},"night_3":{"value":night_3,"color":get_random_color()},"night_4":{"value":night_4,"color":get_random_color()},"night_5":{"value":night_5,"color":get_random_color()},"night_6":{"value":night_6,"color":get_random_color()},"night_7":{"value":night_7,"color":get_random_color()},"night_8":{"value":night_8,"color":get_random_color()},"emoji_":{"value":emoji_},"emoji_1":{"value":emoji_1},"emoji_2":{"value":emoji_2},"emoji_3":{"value":emoji_3},"emoji_4":{"value":emoji_4},"emoji_5":{"value":emoji_5},"emoji_6":{"value":emoji_6},"emoji_7":{"value":emoji_7}}
wm = WeChatMessage(client)
res = wm.send_template(user_id, template_id, data)
print(res)