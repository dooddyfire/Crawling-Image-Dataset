# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 23:00:39 2020

@author: Acer
"""

from selenium import webdriver
import time
import urllib.request
import os
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from tkinter import * 
import threading

def load():
    browser = webdriver.Chrome(ChromeDriverManager().install()) #incase you are chrome
    browser.get('https://www.google.com/')
    search = browser.find_element_by_name('q')
    #keyword = "apple"
    keyword = a.get()
    search.send_keys(keyword,Keys.ENTER)
    elem = browser.find_element_by_link_text('ค้นรูป')
    elem.get_attribute('href')
    elem.click()
    value = 0
    for i in range(20):
       browser.execute_script("scrollBy("+ str(value) +",+1000);")
       value += 1000
       time.sleep(3)
    elem1 = browser.find_element_by_id('islmp')
    sub = elem1.find_elements_by_tag_name('img')
    try:
        os.mkdir('downloads')
    except FileExistsError:
        pass
    
    count = 0
    for i in sub:
        src = i.get_attribute('src')
        try:
            if src != None:
                src  = str(src)
                print(src)
                count+=1
                urllib.request.urlretrieve(src, os.path.join('downloads',keyword+"_"+str(count)+'.jpg'))
            else:
                raise TypeError
        except TypeError:
            print('fail')

def shift(): 
    x1,y1,x2,y2 = canvas.bbox('uno')
    if x2<0 or y1<0:
        x1 = canvas.winfo_width()
        y1 = canvas.winfo_height()//2
        canvas.coords('uno',x1,y1)
    else:
        canvas.move('uno',-2,0)
    canvas.after(1000//fps,shift)

#load("บะหมี่")
if __name__ == '__main__':
    root = Tk()
    root.title("Crawling Picture From Google")
    root.geometry("600x200+0+0")
    root.config(background='powder blue')
    root.resizable(False,False)
    canvas = Canvas(root,bg='black')
    canvas.pack(side=TOP,fill=X)
    textvar = "Developed By Supapong Sakulkoo"
    text = canvas.create_text(0,-2000,text=textvar,tags='uno',font=('Arial',15,'bold'),fill='yellow',anchor='w')
    x1,y1,x2,y2 = canvas.bbox('uno') 
    canvas['width'] = x2-x1
    canvas['height'] = y2-y1
    fps=50
    shift()
    a = StringVar()
    Label(text="Calling Picture",font=('Arial',15,'bold'),fg='black',background='powder blue').pack()
    Label(text="กรอกชื่อรูปภาพ",font=('Arial',15,'bold'),fg='black',background='powder blue').pack(side=LEFT)
    ent = Entry(root,textvariable=a,justify=CENTER,width=30,font=('Arial',20))
    ent.pack(side=LEFT,padx=4,pady=10)
    
    btn = Button(root,text="Download",fg='black',bg='pink',font=('Arial',15,'bold'),command=lambda: threading.Thread(target=load).start())
    
    btn.place(x=200,y=150)
    root.mainloop()