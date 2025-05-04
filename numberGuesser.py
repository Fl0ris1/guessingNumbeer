from tkinter import *
import tkinter.messagebox
import random

remainingLives=3
guess_count=0
guess=0
number=random.randint(1,10)
print(number)
def cmpNumber():
    global remainingLives,guess,guess_count
    while guess!=number and guess_count!=3:
        guess=num_input.get()
        guess=int(guess)
        if guess>number:
            guess_count+=1
            remainingLives-=1
            tkinter.messagebox.showinfo("too high", f"Your guess is too high\nYou have {remainingLives} lives remaining")
            break
            
        elif guess<number:
            guess_count+=1
            remainingLives-=1
            tkinter.messagebox.showinfo("too low",f"Your guess is too low\nYou have {remainingLives} lives remaining")
            break
        else:
            tkinter.messagebox.showinfo("You Won","You Won!!!")

def intro():
    name=name_input.get()
    tkinter.messagebox.showinfo("Instructions",f"Hi {name}, I am picking a number between 1-10. You need to guess that number with only 3 lives.")
    


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

nameBut=Button(root,text="OK",font=("consolas",12,"bold"),bg="#276FBF",fg="#7B8CDE",width=10,command=intro)
nameBut.place(x=200,y=98)

numLbl=Label(root,text="Guess A Number",font=("consolas",12,"bold"),bg="#A5C4D4",fg="#13505B")
numLbl.place(x=10,y=160)

num_input=Entry(root,width=25)
num_input.place(x=10,y=190)

numBut=Button(root,text="GUESS",font=("consolas",12,"bold"),bg="#276FBF",fg="#7B8CDE",width=10,command=cmpNumber)
numBut.place(x=200,y=178)


root.mainloop()