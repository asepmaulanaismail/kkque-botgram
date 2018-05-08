import requests
import sys
import json
import datetime

def monthdelta(date, delta):
    m, y = (date.month+delta) % 12, date.year + ((date.month)+delta-1) // 12
    if not m: m = 12
    d = min(date.day, [31,
        29 if y%4==0 and not y%400==0 else 28,31,30,31,30,31,31,30,31,30,31][m-1])
    return date.replace(day=d,month=m, year=y)

nik = sys.argv[1]
password = sys.argv[2]
token = ""
mydate = datetime.datetime.now()
prevdate = monthdelta(mydate, -1)
currentMonth = mydate.strftime("%B %Y")
prevMonth = prevdate.strftime("%B %Y")

print("Current Month: " + currentMonth)
print("Prev Month: " + prevMonth)

url_auth = "http://ptbsp.ddns.net:13001/auth"
url_send_wr = "http://ptbsp.ddns.net:13001/api/attendance/sendwr"

r = requests.post(url_auth, data={'nik': nik, 'password': password})
response = json.loads(r.text)
token = response["token"]

r = requests.post(url_send_wr + "?token=" + token, data=json.dumps({'nik': nik, 'month': currentMonth, "prevMonth": prevMonth}, separators=(',',':')))
print("Response Send WR: " + r.text)
