#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Break_time notification
# Module
# -schedule
# -time
# -plyer
# -win10toast
# pyinstaller


# In[2]:


from plyer import notification
import plyer 
from win10toast import ToastNotifier
import schedule
import time
import os


# In[3]:


def notification():
    toaster = ToastNotifier()
    return toaster.show_toast("Sample Notification","Python is awesome!!!") 
schedule.every(10).seconds.do(notification) # 3초마다 job 실행
while True:
    schedule.run_pending()
    time.sleep(1)


# In[ ]:


os.getcwd()


# In[ ]:


os.chdir('C:\\workspace\\AUTO_attendence_CHECK_Program\\new')


# In[ ]:


# schedule.every().monday.at("09:49:55").do(notification)
# schedule.every().tuesday.at("09:49:55").do(notification)
# schedule.every().wednesday.at("09:49:55").do(notification)
# schedule.every().thursday.at("09:49:55").do(notification)
# schedule.every().friday.at("09:49:55").do(notification)
# while True:
#     schedule.run_pending()
#     time.sleep(1)


# In[ ]:




