# -*- coding: utf-8 -
from tinydb import TinyDB, Query

db = TinyDB('db/yes_no.json')
db.purge()
db.insert({'text': 'そうだね', 'label': 1})
db.insert({'text': 'YES', 'label': 1})
db.insert({'text': 'OK', 'label': 1})
db.insert({'text': 'はい', 'label': 1})
db.insert({'text': 'そうですね', 'label': 1})
db.insert({'text': 'いいよ', 'label': 1})
db.insert({'text': 'うん', 'label': 1})
db.insert({'text': 'うん、そうだね', 'label': 1})
db.insert({'text': 'はーい', 'label': 1})
db.insert({'text': 'はーいよろしく', 'label': 1})
db.insert({'text': 'はいよ', 'label': 1})
db.insert({'text': 'その通り', 'label': 1})
db.insert({'text': 'イエス', 'label': 1})
db.insert({'text': 'OK', 'label': 1})
db.insert({'text': 'おっけー', 'label': 1})
db.insert({'text': 'おけー', 'label': 1})
db.insert({'text': 'うん大丈夫', 'label': 1})
db.insert({'text': '大丈夫だよー', 'label': 1})
db.insert({'text': '続けて', 'label': 1})
db.insert({'text': '続けてください', 'label': 1})
db.insert({'text': 'うん、続けて', 'label': 1})
db.insert({'text': 'お願いします', 'label': 1})
db.insert({'text': 'いやダメ', 'label': 0})
db.insert({'text': 'いや', 'label': 0})
db.insert({'text': 'だめだな', 'label': 0})
db.insert({'text': '駄目です', 'label': 0})
db.insert({'text': 'いいえ', 'label': 0})
db.insert({'text': 'ちょっと待って', 'label': 0})
db.insert({'text': 'NO', 'label': 0})
db.insert({'text': 'ノー', 'label': 0})
db.insert({'text': 'ダメだよ', 'label': 0})
db.insert({'text': 'だーめ', 'label': 0})
db.insert({'text': 'だーめです', 'label': 0})
db.insert({'text': 'だーめだよー', 'label': 0})
db.insert({'text': 'だめー', 'label': 0})
db.insert({'text': 'だめですー', 'label': 0})
db.insert({'text': 'ダメですね', 'label': 0})
db.insert({'text': 'だめだよ', 'label': 0})
db.insert({'text': '進めない', 'label': 0})
db.insert({'text': '続けない', 'label': 0})
db.insert({'text': 'ストップ', 'label': 0})
db.insert({'text': 'いや違う', 'label': 0})
#
print db.all()
