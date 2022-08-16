import time
import requests
from datetime import datetime

day = 492
i = 0
print(i, day)
def telegram_bot_sendtext(bot_message):

    bot_token = '5342821891:AAGQTMb1iS-Fhc09i5tpn29sBa-L_F5oodk'
    bot_chatID = '-1001228669779'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()



def report():
    global day
    global i
    #i = i + 1
    #strday = str(day + i)
    today = datetime.now()
    start = datetime(2021, 2, 18)
    diff = today.date() - start.date()
    my_message = "D" + str(diff.days) + " di sburo sul trailer di spoon 3" + " https://youtu.be/zgaG88e-Wso"   ## Customize your message
    telegram_bot_sendtext(my_message)

def wait():
        rightnow = datetime.now()
        global sendtime
        ##schedule.run_pending()
        ##time.sleep(1)
        if rightnow.hour == sendtime.hour and rightnow.minute == sendtime.minute: ##remove 2 hours couse fuso orario
            print('message is now sent')
            report()
            time.sleep(60)
            wait()
        else:
            print('Still waiting. Current time is: ',rightnow.hour,':',rightnow.minute)
            time.sleep(60)
            wait()

##schedule.every().day.at("09:00").do(report)
now = datetime.now()
sendtime = datetime.replace(now, hour=8,minute=0 )
while True:
    wait()
