from tkinter import *
import requests
import json


root =Tk()

root.title("Multilingo")
root.geometry("380x250")
root.configure(bg="#1e1f1e")



e=Entry(root,width=50,borderwidth=1)
e.configure(bg="#1e1f1e",fg="white")
e.grid(row=2,column=0,columnspan=3,padx=5,pady=5,ipady=20)
e2=Entry(root,width=50,borderwidth=1)
e2.configure(bg="#1e1f1e",fg="white")
e2.grid(row=4,column=0,columnspan=3,padx=5,pady=5,ipady=20)
title=Label(root,text="Enter the Text:",bg="#1e1f1e",fg="white")
title.grid(row=1,column=0)
tit2=Label(root,text="Translated Text:",bg="#1e1f1e",fg="white")
tit2.grid(row=3,column=0)
tit2.config(font=("Courier", 16))
title.config(font=("Courier", 16))



OPTIONS={"English" : 'en',
         "Spanish": 'es',
         "German":'de',
         "French":'fr',
         "Latin":'la',
         "Greek":'el',
         "Russian":'ru',
         "Romanian":'ro'
         
        }


#initializing variables
var1=StringVar(root)
var=StringVar(root)

#set initial option to English
var.set("English")


#entry box 1
w=OptionMenu(root,var,*OPTIONS)
w["menu"].config(bg="#1e1f1e",fg="white")
w.config(bg="#1e1f1e",fg="white")
w.grid(row=1,column=1)


#entry box2
w1=OptionMenu(root,var1, *OPTIONS)
w1["menu"].config(bg="#1e1f1e",fg="white")
w1.config(bg="#1e1f1e",fg="white")
w1.grid(row=3,column=1)


#to clear the input boxes
def clear() :
   e.delete(0,END)
   e2.delete(0,END)


#translation function
def translate():
 
   
   api_key ='trnsl.1.1.20200411T223236Z.05c15f0fc3539d55.60a083545bcb1fcb925c136ca83d1ec7f4997fab'


   url='https://translate.yandex.net/api/v1.5/tr.json/translate'

   params=dict(key=api_key,text=e.get(),lang=str(OPTIONS.get(var.get()))+'-'+str(OPTIONS.get(var1.get())))
   
  
   res=requests.get(url,params=params)
   json=res.json()
  
   
   e2.insert(0,json['text'][0])
   
#buttons
trans_btn=Button(root,text="translate",command=translate,padx=10,pady=10,bg="#484a48",fg="white")
trans_btn.grid(row=5,column=0,ipadx=40)
clear_btn=Button(root,text="clear",command=clear,padx=10,pady=10,bg="#484a48",fg="white")
clear_btn.grid(row=5,column=1,columnspan=2,ipadx=60)

root.mainloop()


