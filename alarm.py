# Importing all necessary libraries for the alarm project
from tkinter import *
import datetime
import time
import winsound

#Create a while loop 

def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        print("Time set date is: ", date)
        print(now)
        
        if now == set_alarm_timer:
            print("Time to Wake up")
        winsound.PlaySound("sound.wav", winsound.SND_ASYNC)
        break

def actual_time():
    set_alarm_timer = f"{hour.get()}: {min.get()}: {sec.get()}"
    alarm(set_alarm_timer)
        
# Creating GUI using tkinter     
clock = Tk()

clock.title("Python Alarm Clock")
clock.geometry("400x200")

time_format = Label(clock, text= "Enter time in 24 hour format!", fg="white",bg="black",font="Arial").place(x=60, y=120)

addTime = Label(clock,text = "Hour  Min   Sec",font=60).place(x = 110)

setYourAlarm = Label(clock,text = "When to wake you up",fg="blue",relief = "solid",font=("Helevetica",7,"bold")).place(x=0, y=29)

#Variables we require to set the alarm(inizialiation)
hour = StringVar()
min = StringVar()
sec = StringVar()


#Time required to set the alarm clock 
hourTime = Entry(clock, textvariable = hour, bg = "pink", width=15).place(x=110, y= 30)
minTime = Entry(clock, textvariable = min, bg = "pink", width=15).place(x=150,y=30)
secTime = Entry(clock, textvariable = sec, bg = "pink", width=8).place(x=200,y=30)

#To take the time input by the user

submit = Button(clock, text="Set alarm", fg="Blue", width = 10, command = actual_time).place(x=110, y=70)

clock.mainloop()
