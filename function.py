from tkinter import *
import tkinter.messagebox as msgBox
from tkinter.colorchooser import *
from tkinter.filedialog import *

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
 
def closeProgram(root):
        confirm = msgBox.askquestion("ยืนยัน","คุณต้องการปิดโปรแกรมหรือไม่ ?")
        if confirm == "yes":
            root.destroy()   

def selectColor(root):
    color = askcolor()
    print(color)
    # return example ((251.98046875, 70.2734375, 70.2734375), '#fb4646'), access by array index 0,1
    print(color[0])
    print(color[1])
    colorLabel = Label(root,text="Hello Color",fg="black",bg=color[1],font=20).pack()

def selectFile():
    fileOpen = askopenfilename() 
    print(fileOpen)
    fileContent = open(fileOpen)
    fileWindow = Tk()
    fileWindow.title("file content")
    fileWindow.geometry("500x400+0+0")
    myLabel = Label(fileWindow,text=fileContent.read()).pack()
    fileWindow.mainloop()
# Message Box 
def aboutProgram():
    msgBox.showinfo("Infomation Of Program","developer is THTJ") # showInfo มี parameter  ตัวคือ title และ message ที่แสดง