#!/usr/bin/env python
# coding: utf-8

# In[3]:


import schedule
import time

def notification():
    from plyer import notification
    if __name__ == "__main__":
        notification.notify(
        title = "쉬는시간입니다!",
        message = "10분간 몸과 뇌를 새로고침하세요",
        app_name = 'CAKD3',
        app_icon= r'C:\break_icon.ico',
        timeout = 5)
    return
notification()

