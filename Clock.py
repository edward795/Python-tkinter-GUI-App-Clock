#Importing necessary Modules
from tkinter import *
from tkinter.ttk import *
from pytz import timezone
from time import strftime
from datetime import datetime, time

#list to store all time values with 30 mins interval
time_list = ['12:00 AM', '12:30 AM', '01:00 AM', '01:30 AM', '02:00 AM', '02:30 AM', '03:00 AM', '03:30 AM', '04:00 AM', '04:30 AM', '05:00 AM', '05:30 AM', '06:00 AM', '06:30 AM','07:00 AM', '07:30 AM', '08:00 AM', '08:30 AM', '09:00 AM', '09:30 AM', '10:00 AM', '10:30 AM', '11:00 AM', '11:30 AM', '12:00 PM', '12:30 PM', '01:00 PM', '01:30 PM', '02:00 PM', '02:30 PM', '03:00 PM', '03:30 PM', '04:00 PM', '04:30 PM', '05:00 PM', '05:30 PM', '06:00 PM', '06:30 PM', '07:00 PM', '07:30 PM', '08:00 PM', '08:30 PM', '09:00 PM','09:30 PM', '10:00 PM', '10:30 PM', '11:00 PM', '11:30 PM' ]



#initialize root widget & set it' attributes
root = Tk()
root.title('Clock')
root.geometry('300x400')
root.resizable(False, False)
root.configure(background='#34568B')

#initialize a Label Widget to display current IST-EST Timne
lbl = Label(root, font = ('calibri', 20, 'bold'),
            background = '#34568B',
            foreground = 'white',
            width=270)

ist_label=Label(root, font = ('calibri', 12, 'bold'),
            background = '#34568B',
            foreground = 'white',
            width=270)
ist_label.config(text="ist")


est_label=Label(root, font = ('calibri', 12, 'bold'),
            background = '#34568B',
            foreground = 'white',
            width=270)

#Labe1 to display Converted EST Time
estLabel = Label(root, font = ('calibri', 20, 'bold'),
            background = '#34568B',
            foreground = 'white',
            width=270)


#ComboBox to display the 30min interval times
setVar=StringVar(root)
optBox=Combobox(root,width=27,textvariable=setVar)
optBox['values']=time_list
optBox.current(0)


#Display Current IST-EST time within 1s intervals
def time():
    format='%I:%M:%S %p'
    nowIST = strftime(format)
    now=datetime.now(timezone('Asia/Kolkata'))
    nowEST=now.astimezone(timezone('EST')) 
    nowEST=nowEST.strftime(format)
    lbl.config(text = " IST Time: \n"+"    "+nowIST+"\n" + "\n EST Time \n"+"    "+nowEST)
    lbl.after(1000, time)


#Function to convert IST time to EST time
def converISTToEST():
    ist_time=optBox.get()
    now_date=datetime.now(timezone('Asia/Kolkata')).strftime('%b %d %Y')
    ist=str(now_date)+" "+ist_time
    ist_f=datetime.strptime(ist,'%b %d %Y %I:%M %p')
    est=ist_f.astimezone(timezone('EST'))
    est_time=est.strftime(format)
    estLabel.place(x=80,y=320)
    estLabel.config(text=est_time)
    est_label.config(text="est")


#Button to call the convert function
btn=Button(root,text="Convert",command=lambda:converISTToEST())

format='%I:%M:%S %p'
nowIST = strftime(format)

#Packing all components to the UI
btn.place(x=110,y=280)

optBox.place(x=60,y=220)

ist_label.place(x=60,y=190)
est_label.place(x=40,y=320)

lbl.pack(anchor ='center')
time()
 
#Calling eventloop
mainloop()