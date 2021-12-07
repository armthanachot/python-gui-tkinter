from tkinter import *
import function as fn # import file

root = Tk()

root.title("My Windown")

# แสดงข้อความ ด้วย label 
# myLabel1 = Label(root,text="Hello World",fg="red",font=20,bg="black").pack() 
# สร้าง label และใช้ .pack เพื่อบอกว่า ให้แสดงข้อความ พร้อมกับปรับขนาดให้เหมาะกับพื้นที่นั้นๆ และตำแหน่งง default ของ label แบบ .pack คือกลางหน้าจอของ root และใน label มีหลาย properties โดยคั่นด้วย , 
# root คือบอกว่า Label นี้จะทำงานใน root เท่านั้น (อยู่ที่ชื่อตัวแปร)
# text ข้อความ
# fg = foreground คือสีข้อความ
# font ขนาดข้อความ
# bg พื้นหลัง

# กำหนดตำแหน่งของ widget โดยใช้ place , grid
    # place จะเป็นการระบุ XY โดยพิกัดเริ่มต้น 0 0 อยู่มุมซ้ายบน 
    # grid มองเป็นแถว กับคอลัมม์ เหมือนตีตารางในหน้าจอ โดย default row, column เป็น 0 0 จะอยู่ซ้ายบน และหากในหน้าจอของเรามี widget ที่จัดตำแหน่งด้วย pack ทันจะไม่อนุญาตให้ใช้ grid 
# myLabel2 = Label(root,text="My Place",font=20).place(x=125,y=0)

# myLabel3 = Label(root,text="My Grid",font=20).grid(row=1,column=0)

# button 
btn1 = Button(root,text="click me (btn1)",fg="white",bg="black",font=20,command=fn.messageLogging).pack()
# root คือบอกว่า Button นี้จะทำงานใน root เท่านั้น (อยู่ที่ชื่อตัวแปร)
# text ข้อความ
# fg = foreground คือสีข้อความ
# font ขนาดข้อความ
# bg พื้นหลัง
# command คือ function ที่จะให้เรียก หลังจาก click

# textbox
txt = StringVar() # เป็นตัวแปรที่เอาไว้ควบคุม Entry โดยเก็บข้อมูลอยู่ในรูปแบบของ string
myText = Entry(root,textvariable=txt).pack()
# root คือบอกว่า Entry นี้จะทำงานใน root เท่านั้น (อยู่ที่ชื่อตัวแปร)
# textVariable=txt คือบอกว่า ข้อมูลที่ถูก input เข้ามา จะถูกเก็บอยู่ในตัวแปร txt
btn2 = Button(root,text="text logging", fg="black", bg="white", font=20,command=lambda: fn.showSubmittedMessage(txt)).pack()
# ใช้ lambda function หากมีการส่ง argument ถ้าไม่ใช้ จะทำให้ function นั้นถูกเรียกทันที
btn3 = Button(root,text="text display", fg="black", bg="yellow", font=20,command=lambda: fn.displayMessage(root,txt)).pack()
# ใช้ lambda function หากมีการส่ง argument ถ้าไม่ใช้ จะทำให้ function นั้นถูกเรียกทันที
btn4 = Button(root,text="Open Report", fg="black", bg="purple", font=20, command=fn.openReportWindow).pack()
btn5 = Button(root,text="choose color",fg="black",bg="pink",font=20,command=lambda: fn.selectColor(root)).pack()
btn6 = Button(root,text="choose file",fg="black",bg="skyblue",font=20,command=fn.selectFile).pack()

# Menu (toolsbar ด้านบน)

# Menu Items (sub menu)
menuItem = Menu() 
menuItem.add_command(label="New File",command=fn.newFile) # command ใช้สำหรับการ call function เมื่อมีการคลิก
menuItem.add_command(label="Open")
menuItem.add_command(label="Save")
menuItem.add_command(label="About",command=fn.aboutProgram)
menuItem.add_command(label="Exit",command=lambda: fn.closeProgram(root))

# Main menu
myMenu = Menu()
# add menu 
myMenu.add_cascade(label="File",menu=menuItem) # หากมีเมนูย่อย ให้ใช้ property menuItem 
myMenu.add_cascade(label="Help") 

root.config(menu=myMenu)

# กำหนดขนาดหน้าจอ และตำแหน่งหน้าจอ
root.geometry("500x400+0+0") # กว้าง ยาว 500 * 400 ต้องเขียนติดกัน จากนั้น หากมีการกำหนดตำแหน่งของหน้าต่างด้วย ให้ + เพิ่มเข้าไป อ้างอิงตามแกน X และแกน Y โดยจุด 0 0 จะอยู่ที่ มุมซ้ายบน

root.mainloop() # ให้รันวนเรื่อยๆ และระหว่างที่รันอยู่่มันจะคอยเช็คว่า มีการทำ action อะไรบ้าง เช่น เมื่อมีการคลิกปุ่ม จะให้ทำงานอย่างไร


