from tkinter import *
from PIL import Image,ImageTk
import sp2txt
import action
root = Tk()

root.title("AI Assistant")
root.geometry("550x675")
root.resizable(False,False)
root.config(bg="lightblue")

def ask():
    userVal = sp2txt.sp2t()
    botVal = action.action(userVal)
    text.insert(END, "You : " + userVal + "\n")
    if botVal != None:
        text.insert(END,"Bot : " + str(botVal)+ "\n" )
    if botVal == "ok sir":
        root.destroy()

def delete():
    text.delete('1.0',END)
def send():
    user_input = entry.get()
    bot = action.action(user_input)
    text.insert(END, "You : " + user_input + "\n")
    entry.delete(0, END)
    if bot != None:
            text.insert(END,"Bot : " + str(bot)+ "\n" )
    if bot == "ok sir":
          root.destroy()

frame = LabelFrame(root, padx =100,pady= 7, borderwidth=3,relief = "raised")
frame.config(bg="white")
frame.grid(row = 0 , column = 5 , padx = 60 , pady = 10)

textLabel = Label(frame, text="AI Assistant" , font=("comic sans ms", 14, "bold"), bg="white")
textLabel.grid(row = 0 , column = 0, padx = 20 , pady = 10)

imageAI = ImageTk.PhotoImage(Image.open("C:\\Users\\HP\\Desktop\\coding\\PythonFiles\\intermediate_Prjct\\Personalised\\pic.jpeg"))
imageLabel = Label(frame, image=imageAI)
imageLabel.grid(row =1 , column =0 ,pady= 20 )

text = Text(root , font = ("courier 10 bold ") ,  bg= "#356696")
text.grid(row= 1, column=0)
text.place(x=100,y=375,width=375,height=100)

entry = Entry(root,justify=CENTER)
entry.place(x=100,y=500,width =350,height=30)

Btn1 = Button(root , text = "Say", bg="#356696", pady =16 ,padx = 40,borderwidth=3, relief=SOLID,command = ask)
Btn1.place(x=70,y = 575)

Btn2 = Button(root , text = "Delete", bg="#356696", pady =16 ,padx = 40,borderwidth=3, relief=SOLID,command = delete)
Btn2.place(x=205,y = 575)

Btn3 = Button(root , text = "Send", bg="#356696", pady =16 ,padx = 40,borderwidth=3, relief=SOLID,command = send)
Btn3.place(x=350,y = 575)
root.mainloop()
 