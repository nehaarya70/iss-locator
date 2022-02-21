import json
import urllib.request
#import turtle
import time
from tkinter import *
import matplotlib.pyplot as plt
#from scipy.misc import imread
from matplotlib.pyplot import imread


root=Tk()
root.geometry("850x400")
root.title("Welcome")
root.config(bg="alice blue")

lb=Label(root,width=35,text=" Space Station Locator ",bg="peach puff",
                     relief="solid",font="times 25",justify="center")
lb.place(x=90,y=20)


def who():
    raj=Tk()
    raj.title('People in Space')
    url='http://api.open-notify.org/astros.json'
    response=urllib.request.urlopen(url)
    result=json.loads(response.read())

    sb=Scrollbar(raj)
    sb.pack(side=RIGHT ,fill=Y)
    mylist=Listbox(raj,width=50,yscrollcommand=sb.set)

    mylist.insert(END,'Total People In Space='+str(result['number']))
    people=result['people']

    for p in people:
        mylist.insert(END,p['name']+' in '+p['craft'])
    mylist.pack(side=LEFT, fill=BOTH,expand=True)
    sb.config(command=mylist.yview)
    raj.mainloop()

def where():

    url='http://api.open-notify.org/iss-now.json'
    response=urllib.request.urlopen(url)
    result=json.loads(response.read())


    location=result['iss_position']
    lat=location['latitude']
    lon=location['longitude']
    print('Latitude:',lat)
    print('Longitude:',lon)
    lat=float(lat)
    lon=float(lon)

    x=plt.xlim(-180,180)
    y=plt.ylim(-90,90)
    img=imread('Downloads\earth.png')
    plt.scatter(lon,lat)
    plt.imshow(img,zorder=0,extent=[-180,180,-90,90])
    plt.tight_layout()
    plt.show()


    
def when():
    rine=Tk()
    rine.title('Overhead Passes')
    lb1=Listbox(rine)
    lat=31.577527
    lon=74.99155080000003

    url='http://api.open-notify.org/iss-pass.json'
    url=url+'?lat='+str(lat)+'&lon='+str(lon)
    response=urllib.request.urlopen(url)
    result=json.loads(response.read())

    sb=Scrollbar(rine)
    sb.pack(side=RIGHT, fill=Y)
    mylist=Listbox(rine,yscrollcommand=sb.set,width=50)
    
    response=result['response']
    for r in response:
        mylist.insert(END,time.ctime(r['risetime']))
    mylist.pack(side=LEFT,fill=BOTH)
    sb.config(command=mylist.yview)
    rine.mainloop()


b1=Button(root,text='click here',command=who,relief='flat',font='times 18',
                 bg='alice blue',justify='left')
b2=Button(root,text='click here',command=where,relief='flat',font='times 18',
                 bg='alice blue')
b3=Button(root,text='click here',command=when,relief='flat',font='times 18',
                 bg='alice blue')


lb1=Label(root,text='To Know Who is in Space',width=25,bg='alice blue',
                      font='times 20',justify='right')
lb2=Label(root,text='To Know Where is The ISS',bd=1,width=25,bg='alice blue',
                      font='times 20',justify='right')
lb3=Label(root,text='To Know When Will The ISS Be Overhead Our ACET',bg='alice blue',
                      font='times 20',justify='left')


lb1.place(x=0,y=140)
lb2.place(x=0,y=200)
lb3.place(x=0,y=260)
b1.place(x=400,y=135)
b2.place(x=400,y=195)
b3.place(x=620,y=255)
              
root.mainloop()
