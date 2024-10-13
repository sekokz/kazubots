import random
from datetime import datetime

items = [
   {"date": "6-19", "name": "一柳梨璃"},
   {"date": "4-12", "name": "白井夢結"},
   {"date": "1-1", "name": "楓・J・ヌーベル"},
   {"date": "12-21", "name": "二川二水"},
   {"date": "2-13", "name": "安藤鶴紗"},
   {"date": "7-21", "name": "吉村・Thi・梅"},
   {"date": "2-6", "name": "郭神琳"},
   {"date": "12-21", "name": "王雨嘉"},
   {"date": "11-25", "name": "ミリアム"},
   {"date": "8-13", "name": "相澤一葉"},
   {"date": "3-27", "name": "佐々木藍"},
   {"date": "5-4", "name": "飯島恋花"},
   {"date": "11-7", "name": "初鹿野瑤"},
   {"date": "10-2", "name": "芹沢千香瑠"},
   {"date": "10-31", "name": "今叶星"},
   {"date": "5-21", "name": "宮川高嶺"},
   {"date": "6-8", "name": "土岐紅巴"},
   {"date": "9-24", "name": "丹羽灯莉"},
   {"date": "3-3", "name": "定盛姫歌"},
   {"date": "10-27", "name": "天野天葉"},
   {"date": "9-19", "name": "真島百由"},
   {"date": "1-11", "name": "番匠谷依奈"},
   {"date": "4-25", "name": "遠藤亜羅椰"},
   {"date": "11-3", "name": "田中壱"},
   {"date": "3-27", "name": "江川樟美"},
   {"date": "10-2", "name": "金箱弥宙"},
   {"date": "", "name": "一柳結梨"},
   {"date": "8-11", "name": "渡邉茜"},
   {"date": "6-21", "name": "高須賀月詩"},
   {"date": "12-25", "name": "船田純"},
   {"date": "12-25", "name": "船田初"},
   {"date": "12-15", "name": "岸本・L・来夢"},
   {"date": "4-22", "name": "福山・J・幸恵"},
   {"date": "7-22", "name": "森辰姫"},
   {"date": "6-19", "name": "川村楪"},
   {"date": "6-25", "name": "月岡椛"},
   {"date": "8-22", "name": "藤田槿"},
   {"date": "4-15", "name": "六角汐里"},
   {"date": "3-9", "name": "黒木・F・百合亜"},
   {"date": "5-25", "name": "天宮・S・聖恋"},
   {"date": "2-2", "name": "松永・B・佳世"},
   {"date": "7-12", "name": "秦祀"},
   {"date": "4-2", "name": "伊東閑"},
   {"date": "7-30", "name": "立原紗癒"},
   {"date": "12-15", "name": "王莉芬"},
   {"date": "3-26", "name": "横田悠夏"},
   {"date": "2-25", "name": "本間秋日"},
   {"date": "11-21", "name": "石塚藤乃"},
   {"date": "6-13", "name": "塩崎鈴夢"},
   {"date": "2-9", "name": "牧野美岳"},
   {"date": "3-5", "name": "賀川蒔菜"},
   {"date": "10-15", "name": "松村優珂"},
   {"date": "4-5", "name": "森本結爾"},
   {"date": "5-1", "name": "倉又雪陽"},
   {"date": "8-8", "name": "妹島広夢"},
   {"date": "5-10", "name": "苅谷緋紅"},
   {"date": "2-17", "name": "早川弥宏"},
   {"date": "8-6", "name": "富永真"},
   {"date": "5-15", "name": "高松祇恵良"},
   {"date": "1-2", "name": "槇若菜"},
   {"date": "3-22", "name": "毛綱乃彩"},
   {"date": "7-7", "name": "山梨日羽梨"},
   {"date": "5-15", "name": "岡田綺更"},
   {"date": "3-24", "name": "多田紫恵楽"},
   {"date": "9-25", "name": "高島八雲"},
   {"date": "7-3", "name": "川添美鈴"},
   {"date": "9-6", "name": "菱田治"},
   {"date": "3-19", "name": "坪井七保"}
  ]

def get_lily(name):
    
    today = datetime.now().strftime("%m-%d")

    match_names = [entry["name"] for entry in items if entry["date"] == today]

    if match_names:
      msg = f"今日は {' ちゃんと '.join(match_names)} ちゃんの誕生日！"
    else:
      random_name = random_lily()
      msg = f"{name}さんの今日のリリィは {random_name["name"]} だよ"
    return msg

def random_lily():
  result = random.choices(items)[0]
  return result
