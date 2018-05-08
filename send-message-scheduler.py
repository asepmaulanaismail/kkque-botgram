import requests
import time
import datetime
import sys

# @xlvlayana_bot token
bot_token = sys.argv[1]
url = "https://api.telegram.org/bot" + bot_token + "/sendMessage"
chat_id = sys.argv[2] # marbel
gmt = 7

debug = False
counter = 1
while(True):
    if debug == True:
        r = requests.post(url, data={'chat_id': chat_id, 'text': "test *bold*", 'parse_mode': "Markdown"})
        
    now = datetime.datetime.now()

    pesan = ""
    if now.hour+gmt == 5 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Shubuh* yaa"
    elif now.hour+gmt == 12 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Dhuhur* yaa"
    elif now.hour+gmt == 15 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Ashar* yaa"
    elif now.hour+gmt == 18 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Magrib* yaa"
    elif now.hour+gmt == 19 and now.minute == 0:
        pesan = "Jangan lupa *Sholat Isya* yaa"

    print("now: " + str(now.hour) + ":" + str(now.minute))
    
    if pesan != "":
        r = requests.post(url, data={'chat_id': chat_id, 'text': pesan, 'parse_mode': "Markdown"})

    time.sleep(1)