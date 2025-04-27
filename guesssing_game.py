from tkinter import *
import tkinter.messagebox
import random

remainingLives=3

number=random.randint(0,10)

def cmpNumber():
    global remainingLives
    while guess!=number and remainingLives!=0:
        guess=int(num_input.get())
        if guess>number:
            remainingLives-=1
            tkinter.messagebox.showinfo("too high", f"Your guess is too high\nYour have {remainingLives} lives remaining")
            
        
        elif guess<number:
            remainingLives-=1
            tkinter.messagebox.showinfo("too low",f"your guess is too low\nYou have {remainingLives} lives remaining")
        else:
            tkinter.messagebox.showinfo("You Won","You Won!!!")
    
    
root=Tk()
root.geometry("350x300")
root.title("Guessing Game")
root.config(background="#A5C4D4")

titleLbl=Label(root,text="Welcome To The Game",font=("consolas",16,"bold"),bg="#A5C4D4",fg="#101D42")
titleLbl.pack()

nameLbl=Label(root,text="What Is Your Name?",font=("consolas",12,"bold"),bg="#A5C4D4",fg="#13505B")
nameLbl.place(x=10,y=80)

name_input=Entry(root,width=25)
name_input.place(x=10,y=110)

nameBut=Button(root,text="OK",font=("consolas",12,"bold"),bg="#276FBF",fg="#7B8CDE",width=10)
nameBut.place(x=200,y=98)

numLbl=Label(root,text="Guess A Number",font=("consolas",12,"bold"),bg="#A5C4D4",fg="#13505B")
numLbl.place(x=10,y=160)

num_input=Entry(root,width=25)
num_input.place(x=10,y=190)

numBut=Button(root,text="GUESS",font=("consolas",12,"bold"),bg="#276FBF",fg="#7B8CDE",width=10)
numBut.place(x=200,y=178)


root.mainloop()