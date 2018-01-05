#TicTacToe GUI
#created by github.com/1998

from tkinter import *
from tkinter import messagebox

turn = 1

def gamePage():
    startframe.destroy()
    button1 = Button(frame, text="", command=lambda: cheak(button1))
    button2 = Button(frame, text="", command=lambda: cheak(button2))
    button3 = Button(frame, text="", command=lambda: cheak(button3))
    button4 = Button(frame, text="", command=lambda: cheak(button4))
    button5 = Button(frame, text="", command=lambda: cheak(button5))
    button6 = Button(frame, text="", command=lambda: cheak(button6))
    button7 = Button(frame, text="", command=lambda: cheak(button7))
    button8 = Button(frame, text="", command=lambda: cheak(button8))
    button9 = Button(frame, text="", command=lambda: cheak(button9))

    button1.place(x=10, y=10, width=50, height=50)
    button2.place(x=60, y=10, width=50, height=50)
    button3.place(x=110, y=10, width=50, height=50)
    button4.place(x=10, y=60, width=50, height=50)
    button5.place(x=60, y=60, width=50, height=50)
    button6.place(x=110, y=60, width=50, height=50)
    button7.place(x=10, y=110, width=50, height=50)
    button8.place(x=60, y=110, width=50, height=50)
    button9.place(x=110, y=110, width=50, height=50)

    frame.pack()

    def cheak(button):
        global turn
        if turn % 2 == 1:
            button["text"] = "X"
            turn += 1
        else:
            button["text"] = "0"
            turn += 1
        if button1["text"] == button2["text"] == button3["text"]:
            label.config(text="{} Wins".format(button2["text"]))
        elif button4["text"] == button5["text"] == button6["text"]:
            label.config(text="{} Wins".format(button4["text"]))
        elif button7["text"] == button8["text"] == button9["text"]:
            label.config(text="{} Wins".format(button9["text"]))
        elif button1["text"] == button4["text"] == button7["text"]:
            label.config(text="{} Wins".format(button4["text"]))
        elif button2["text"] == button5["text"] == button8["text"]:
            label.config(text="{} Wins".format(button2["text"]))
        elif button3["text"] == button6["text"] == button9["text"]:
            label.config(text="{} Wins".format(button9["text"]))
        elif button1["text"] == button5["text"] == button9["text"]:
            label.config(text="{} Wins".format(button9["text"]))
        elif button3["text"] == button5["text"] == button7["text"]:
            label.config(text="{} Wins".format(button5["text"]))


root = Tk()
root.title("TicTacToe")
frame = Frame(root,bg="blue",width=300,height=300)
startframe = Frame(root,bg="blue",width=200,height=100)

label = Label(frame, text="WELCOME", fg="white", bg="blue")
label.place(x=180, y=60, width=100, height=20)
startButton = Button(startframe, text="START", bg="Green", fg="white",command=gamePage)
startButton.place(x=80, y=40, width=50, height=20)
startframe.pack()

root.mainloop()
