#!/usr/bin/env python
# coding: utf-8

# In[20]:


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


# In[28]:



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
        message = "<14:00 - 14:48> 중 랜덤으로\n<1회> 신호출결이 진행됩니다",
        app_name = 'CAKD3',
        app_icon= 'check.ico',
        timeout = 5)
    return



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


# In[29]:


#checking
prog_s()


#QR
schedule.every().day.at("08:50:00").do(QR)
schedule.every().day.at("09:00:00").do(class_start)
schedule.every().day.at("09:49:57").do(break_time)


schedule.every().day.at("09:03:30").do(class_start)
schedule.every().day.at("10:00:00").do(class_start)
schedule.every().day.at("10:49:57").do(break_time)


schedule.every().day.at("11:00:00").do(class_start)
schedule.every().day.at("11:49:57").do(break_time)


schedule.every().day.at("12:00:00").do(class_start)
schedule.every().day.at("12:49:55").do(lunch)

schedule.every().day.at("13:59:55").do(check)
schedule.every().day.at("14:00:00").do(class_start)
schedule.every().day.at("14:49:57").do(break_time)


schedule.every().day.at("14:59:57").do(class_start)
schedule.every().day.at("15:49:57").do(break_time)


schedule.every().day.at("16:00:00").do(class_start)
schedule.every().day.at("16:49:57").do(break_time)


schedule.every().day.at("17:00:00").do(class_start)
schedule.every().day.at("17:50:00").do(QR)

while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:




