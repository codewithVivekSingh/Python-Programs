"""This is a rolling dice game. Each time you clicks the button, a random number will be shown on the dice"""
"""To run this code, you will require six dice images and a sound file"""
import random
from tkinter import *
from PIL import Image, ImageTk
import playsound

mainWindow=Tk()
mainWindow.title("Roll a dice")
mainWindow.geometry("400x800")

def myClick():
    playsound.playsound("sound.mp3", False)
    diceNumber=random.randint(1,6)
    if diceNumber==1:
        image1 = Image.open("dice 1.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 1", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")


    elif diceNumber==2:
        image1 = Image.open("dice 2.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 2", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")


    elif diceNumber==3:
        image1 = Image.open("dice 3.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 3", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")

    elif diceNumber==4:
        image1 = Image.open("dice 4.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 4", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")

    elif diceNumber==5:
        image1 = Image.open("dice 5.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 5", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")

    elif diceNumber==6:
        image1 = Image.open("dice 6.jpg")
        test = ImageTk.PhotoImage(image1)
        label1 =Label(image=test)
        label1.image = test
        label1.place(x=50, y=0)
        label2=Label(mainWindow, text="You got 6", font="Verdana 18").place(x=150, y=300)
        button1.config(text="Roll again")




button1 = Button(mainWindow, text="Roll Dice",font=("Calibri 18"), command=myClick, padx=50, pady=10, bd=5, bg="yellow", fg="Black")
button1.place(x=110,y=400)

        


mainWindow.mainloop()











