#!/usr/bin/env python
# coding: utf-8

# In[1]:


# module import
from plyer import notification
import schedule
import time
import pyautogui
import tkinter as tk
from tkinter import filedialog
import os
import datetime as dt
import webbrowser
import numpy as np


# In[2]:


def programe_start():
    if __name__ == "__main__":
        notification.notify(
        title = "프로그램 실행!",
        message = "자동 알림 프로그램 실행완료.",
        app_name = 'CAKD3',
        app_icon= 'emoji.ico',
        timeout = 5)
    return


def break_time():
    if __name__ == "__main__":
        notification.notify(
        title = "쉬는시간입니다!",
        message = "10분간 몸과 뇌를 새로고침하세요",
        app_name = 'CAKD3',
        app_icon= 'clock_icon.ico',
        timeout = 5)
    return


def lunch():
    if __name__ == "__main__":
        notification.notify(
        title = "점심시간입니다!",
        message = "14:00까지 식사하고 쉬고 오세요",
        app_name = 'CAKD3',
        app_icon= 'lunch.ico',
        timeout = 5)
    return


def check():
    if __name__ == "__main__":
        notification.notify(
        title = "신호출결!",
        message = "신호출결을 하시기 바랍니다!\n<14:00 - 14:48> 중 랜덤으로\n 1회 신호출결이 진행됩니다",
        app_name = 'CAKD3',
        app_icon= 'check.ico',
        timeout = 5)
    return

def random_minute():
    return np.random.randint(3,40)

min_ = random_minute()
random_check = dt.time(14,int(f'{min_}'),00).strftime('%H:%M:%S')

#Test
# def random_minute():
#     return np.random.randint(38,40)

# min_ = random_minute()
# random_check = dt.time(2,int(f'{min_}'),00).strftime('%H:%M:%S')
# Test complited



def class_start():
    if __name__ == "__main__":
        notification.notify(
        title = "수업시작!",
        message = "자리에 앉아 코딩합시다",
        app_name = 'CAKD3',
        app_icon= 'board.ico',
        timeout = 5)
    return


def QR():
    from PIL import Image
    if __name__ == '__main__':
        im = Image.open('qrcode.png')
        im.show()     
        
def prog_s():
    if __name__ == "__main__":
        notification.notify(
        title = "프로그램!",
        message = "자동프로그램이 시작됩니다.",
        app_name = 'CAKD3',
        app_icon= 'emoji.ico',
        timeout = 5)
    return


# In[ ]:


#checking
prog_s()


#QR
schedule.every().day.at("08:50:00").do(QR)
schedule.every().day.at("09:00:00").do(class_start)
schedule.every().day.at("09:49:57").do(break_time)

schedule.every().day.at("10:00:00").do(class_start)
schedule.every().day.at("10:49:57").do(break_time)
 

schedule.every().day.at("11:00:00").do(class_start)
schedule.every().day.at("11:49:57").do(break_time)


schedule.every().day.at("12:00:00").do(class_start)
schedule.every().day.at("12:49:55").do(lunch)

schedule.every().day.at("14:00:00").do(class_start)
schedule.every().day.at(f"{random_check}").do(check)
schedule.every().day.at("14:49:57").do(break_time)


schedule.every().day.at("14:59:57").do(class_start)
schedule.every().day.at("15:49:57").do(break_time)


schedule.every().day.at("16:00:00").do(class_start)
schedule.every().day.at("16:49:57").do(break_time)


schedule.every().day.at("17:00:00").do(class_start)
schedule.every().day.at("17:50:00").do(QR)


schedule.every().day.at(f"{random_check}").do(QR)


while True:
    schedule.run_pending()
    time.sleep(1)


# ### Program log
# - 1.0.2 beta - stabilized 1.0.1 beta (21.08.26)
# - 1.0.1 beta - check at random_time between from 14:00 to 14:40 (21.08.26)
# - 1.0.0 alpha - notificaion / QR / check / lunch / capture | class_start  (21.08.20)

# #### Need develop
# 
# 1. Widget by tkinter or usage python based gui 
# 2. Using Zoom api
#     2-1. auto_drive zoom program
#     2-2. auto_screen share at 08:50 with QR
#     2-3. message / or chat bot
# 3. Sound recognition by python module
#     3-1. using zoom_api, python recogize specific sound "신호 전송" | "신호 출결" and send message to chat
# 

# In[ ]:




