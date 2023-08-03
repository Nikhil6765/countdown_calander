from tkinter import Tk, Canvas
from datetime import date, datetime

# getting data from events.txt file
def get_events():
    list_events=[]
    with open('events.txt') as file:  # this line opens the text file
        for line in file:
            line=line.rstrip('\n') # removes the new line character '\n' from each line
            current_event=line.split(',') # split each event into two parts 
            event_date=datetime.strptime(current_event[1], '%d/%m/%y').date()  # turns the second item in the line from a strinf to date
            current_event[1]=event_date  #sets the second item in the list to be the date of the event
            list_events.append(current_event)
    return list_events

# creating a function to count number of days

def days_between_dates(date1,date2):
    time_between=str(date1-date2)
    number_of_days=time_between.split(' ') # here the string is spltted at each blank space
    return number_of_days[0]

# creating the canvas 

root=Tk()  # creating a tkinter window

c=Canvas(root, width=1000, height=500, bg='black')  # canvas of 800 by 800 created

c.pack()  # packs the canvas into tkinter window

c.create_text(100,50,anchor='w',fill='orange',font='Arial 28 bold underline', text='My Countdown Calander')  # this line adds text onto the c canvas

events=get_events()
today=date.today()
vertical_space=100
events.sort(key=lambda x:x[1])  # this sorts the list in order of days to go and not by the name of the events

for event in events:
    event_name=event[0]
    days_untill=days_between_dates(event[1],today)
    display='It is %s days untill %s '%(days_untill,event_name)
    if (int(days_untill)<=7):
        text_col='red'
    else:
        text_col='lightblue'

    c.create_text(100,vertical_space,anchor='w',fill=text_col,font='Arial 28 bold ', text=display)  # this line adds text onto the c canvas
    vertical_space=vertical_space+50

root.mainloop()
