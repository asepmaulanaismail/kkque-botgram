import requests
import time
import datetime
import sys
from datetime import date
import calendar
from random import randint

# @xlvlayana_bot token
bot_token = sys.argv[1]
url = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
chat_id = sys.argv[2] # marbel
gmt = 7

debug = False
counter = 1

todayDate = date.today()
day = calendar.day_name[todayDate.weekday()]

strSecondaryChat = ["Jangan lupa doain aku juga", "Udah doain orang tua juga kan?", "Gausah cepet-cepet sholatnya, aku tungguin kok.", "Pahala shalat berjamaah dibanding shalat sendirian adalah 27 derajat, lebih utama shalat berjamaah.", "Kerja itu cuma selingan sambil nunggu waktu shalat", "Duduk berjam-jam buat ngopi aja bisa, masa shalat cuma 5 menit gak bisa?", "hayu geura sholat aih!!!" ]

while(True):
    if debug == True:
        r = requests.post(url, data={'chat_id': chat_id, 'text': "test *bold*", 'parse_mode': "Markdown"})
        
    now = datetime.datetime.now()

    pesan = ""
    if now.hour+gmt == 5 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Subuh* yaa" + ", " + strSecondaryChat[randint(0,6)]
    elif (now.hour+gmt == 11 and now.minute == 30 and 
       todayDate.strftime("%A").lower() == "friday"):
        pesan = "Yuk *Sholat Jumat* dulu, barang siapa yang mengerjakan sholat jumat dihari sabtu sesungguhnya ia adalah orang yang tersesat."
    elif now.hour+gmt == 12 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Dhuhur* yaa" + ", " + strSecondaryChat[randint(0,6)]
    elif now.hour+gmt == 15 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Ashar* yaa" + ", " + strSecondaryChat[randint(0,6)]
    elif now.hour+gmt == 18 and now.minute == 0:
        pesan = "Selamat Menunaikan Ibadah Solat Magrib *Kesayangan* :heart_eyes: " + ", " + strSecondaryChat[randint(0,6)]
    elif now.hour+gmt == 19 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Isya* yaa :heart: " + ", " + strSecondaryChat[randint(0,6)]

    print("now: " + str(now.hour) + ":" + str(now.minute))
    
    if pesan != "":
        r = requests.post(url, data={'chat_id': chat_id, 'text': pesan, 'parse_mode': "Markdown"})

    time.sleep(60)
