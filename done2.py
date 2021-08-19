#!/usr/bin/env python
# coding: utf-8

# In[1]:


import warnings
warnings.filterwarnings('ignore')
try:
    import schedule
    import time
    import pyautogui
    import tkinter as tk
    from tkinter import filedialog
    import os
    import datetime as dt
    from tkinter import ttk
    import webbrowser 
except ImportError:
    from pip._internal import main as pip
    pip(['install', '--user', 'schedule','pyautogui'])
    import schedule
    import pyautogui


# In[2]:


# module import

import schedule
import time
import pyautogui
import tkinter as tk
from tkinter import filedialog
import os
import datetime as dt
from tkinter import ttk
import webbrowser


# In[3]:


def notification():
    from plyer import notification
    if __name__ == "__main__":
        notification.notify(
        title = "쉬는시간입니다!",
        message = "10분간 몸과 뇌를 새로고침하세요",
        app_name = 'CAKD3',
        app_icon= 'clock_icon.ico',
        timeout = 5)
    return


def lunch():
    from plyer import notification
    if __name__ == "__main__":
        notification.notify(
        title = "점심시간입니다!",
        message = "14:00까지 식사하고 쉬고 오세요",
        app_name = 'CAKD3',
        app_icon= 'lunch.ico',
        timeout = 5)
    return


def check():
    from plyer import notification
    if __name__ == "__main__":
        notification.notify(
        title = "신호출결!",
        message = "신호출결할 시간입니다.",
        app_name = 'CAKD3',
        app_icon= 'check.ico',
        timeout = 5)
    return



def capture():
    from plyer import notification
    if __name__ == "__main__":
        notification.notify(
        title = "화면캡쳐!",
        message = "화면캡쳐할 시간입니다.",
        app_name = 'CAKD3',
        app_icon= 'capture.ico',
        timeout = 5)
    return






def magic():
    if __name__ == '__main__':
        root = tk.Tk()
        root.title("마법사..랄까?")
        root.geometry("250x100+100+900")
        canvas1 = tk.Canvas(root,width=300,height=50)

        canvas1.pack()

        def takeScreenshot():
            myScreenshot = pyautogui.screenshot()
            now = dt.datetime.now().strftime("%Y-%m-%d %H")

#             file_path = filedialog.saveasfilename(initialdir='C:/workspace/',initialfile = f"화면 캡처 {now}시", defaultextension='.png')
        #     file_path = filedialog.asksaveasfilename(initialdir='C:/workspace/', title='Save File', filetypes=(('png Files', 'png.*'), ('All Files', '*.*')))

            myScreenshot.save(f'C:\화면 캡처 {now}시.png') # directory 변경
            os.startfile('C:/') # dorectory 변경
            webbrowser.open_new_tab("https://drive.google.com/drive/folders/1SgyRIMz4sqFhLcaGUY9RF04eNpTtlCKC")


        myButton = tk.Button(text="캡처",command=takeScreenshot,bg='skyblue',fg='black',font=20, height = 2 , width = 10, compound='c')
        
#         canvas1.create_window(125,20,window=myButton)
        canvas1.create_window(125,20,window=myButton)
#         myButton1 = tk.Button(text="저장폴더열기",command=open_folder,bg='lightblue',fg='black',font=10)    
#         canvas1.create_window(200,20,window=myButton1)    
 
        label = ttk.Label(text = "버튼을 누르시면 전체화면 캡처가 저장되고\n저장폴더와 화면캡쳐 드라이브가 열립니다.",
                         padding = (0,0))
        
        label.pack()
            


        root.mainloop()



def QR():
    from PIL import Image
    if __name__ == '__main__':
        im = Image.open('qrcode.png')
        im.show()            
    


# In[ ]:


#QR
schedule.every().day.at("08:50:00").do(QR)
schedule.every().day.at("17:50:00").do(QR)

#check
schedule.every().day.at("09:59:57").do(check)
schedule.every().day.at("14:59:57").do(check)

#lunch
schedule.every().day.at("12:49:55").do(lunch)


#capture
schedule.every().day.at("11:00:00").do(capture)
schedule.every().day.at("11:00:00").do(magic)

schedule.every().day.at("12:00:00").do(capture)
schedule.every().day.at("12:00:00").do(magic)

schedule.every().day.at("14:00:00").do(capture)
schedule.every().day.at("14:00:00").do(magic)

schedule.every().day.at("16:00:00").do(capture)
schedule.every().day.at("16:00:00").do(magic)

schedule.every().day.at("17:00:00").do(capture)
schedule.every().day.at("17:00:00").do(magic)





#notification

#imported QR
schedule.every().day.at("09:49:57").do(notification)
#imported check
schedule.every().day.at("10:49:57").do(notification)
#imported capture 
schedule.every().day.at("11:49:57").do(notification)
#imported capture 

#imported lunch

#imported capture 
schedule.every().day.at("14:49:57").do(notification)
schedule.every().day.at("15:49:57").do(notification)
#imported capture 
schedule.every().day.at("16:49:57").do(notification)
#imported capture 



##TEST
schedule.every().day.at("00:58:00").do(QR)
schedule.every().day.at("00:58:30").do(check)
schedule.every().day.at("00:59:00").do(notification)
schedule.every().day.at("00:59:30").do(lunch)
schedule.every().day.at("01:00:00").do(capture)
schedule.every().day.at("01:25:00").do(magic)


while True:
    schedule.run_pending()
    time.sleep(1)

