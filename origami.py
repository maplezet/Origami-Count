import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *
import tkinter as tk

#datasheet section
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("origami count").sheet1

#global var
button_flag = True
isCrane = True

crane_amount_buffer = 0
lil_crane_amount_buffer = 0

crane_amount = int(sheet.cell(1,2).value)
lil_crane_amount = int(sheet.cell(2,2).value)

sol1 = crane_amount + crane_amount_buffer
sol2 = lil_crane_amount + lil_crane_amount_buffer

#command
def craneClicked():
    global isCrane
    global button_flag
    if button_flag == True:
        button_flag = False
        isCrane = False

        button1.config(image=lil_crane)

        label1.config(text=sol2)
    else:
        button_flag = True
        isCrane = True

        button1.config(image=crane)

        label1.config(text=sol1)



def addCrane():
    global crane_amount_buffer
    global lil_crane_amount_buffer
    global sol1
    global sol2
    if isCrane == True:
        sol1 +=1
        label1.config(text=sol1)
    else:
        sol2 +=1
        label1.config(text=sol2)

def delCrane():
    global crane_amount_buffer
    global lil_crane_amount_buffer
    global sol1
    global sol2
    if isCrane:
        sol1 -=1
        label1.config(text=sol1)
    else:
        sol2 -= 1
        label1.config(text=sol2)

def push():
    sheet.update_cell(1,2,sol1)
    sheet.update_cell(2,2,sol2)

def callback():
    push()
    root.destroy()
    
 
#gui

root = tk.Tk()
root.geometry('400x600')
root.resizable(0,0)
root.configure(bg='#C9F6FF')
root.title("Crane Counter")
root.protocol("WM_DELETE_WINDOW", callback)


crane = PhotoImage(file="assets/crane.png")
lil_crane = PhotoImage(file="assets/lil crane.png")
next1 = PhotoImage(file="assets/next.png")
back = PhotoImage(file="assets/back.png")
refresh = PhotoImage(file="assets/refresh.png")

r_back = back.subsample(10, 10) 
r_refresh = refresh.subsample(10, 10) 
r_next = next1.subsample(10, 10) 
 
label1 = Label(root, text=crane_amount, bg='#C9F6FF')
label1.config(font=("San Francisco", 30))
label1.pack(padx=10, pady=10)

button1 = Button(root, bg='#C9F6FF', image=crane, height=300, width=400, borderwidth=0, activebackground='#C9F6FF', command=craneClicked)
button1.pack()

Frame3 = Frame(root, bg='#C9F6FF')

button2 = Button(Frame3, text="back", image=r_back, bg='#C9F6FF', activebackground='#C9F6FF', borderwidth=0, height=70, width=70, command=delCrane)
button2.pack(side=LEFT, padx=20,)
button3 = Button(Frame3, text="refresh", image=r_refresh, bg='#C9F6FF', activebackground='#C9F6FF', borderwidth=0, height=70, width=70, command=push)
button3.pack(side=LEFT, padx=20)
button4 = Button(Frame3, text="next", image=r_next, bg='#C9F6FF', activebackground='#C9F6FF', borderwidth=0, height=70, width=70, command=addCrane)
button4.pack(side=LEFT, padx=20)

Frame3.pack(expand=1)

#display
root.mainloop()

