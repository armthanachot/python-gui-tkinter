from tkinter import *
import tkinter.messagebox as msgBox

def messageLogging():
        print("Hello this is message")

def showSubmittedMessage(msg):
        print(msg.get())
        print(msg)

def displayMessage(root,msg):
    Label(root,text=msg.get(),fg="red",font=30,bg="black").pack()

def openReportWindow():
    report = Tk()
    report.title("Report")
    report.geometry("500x300")


# Menu 
def newFile():
        window = Tk() 
        window.title("New File")
        window.mainloop()
    

# Message Box 
def aboutProgram():
    msgBox.showinfo("Infomation Of Program","developer is THTJ") # showInfo มี parameter  ตัวคือ title และ message ที่แสดง