from tkinter import *
from tkinter import messagebox as mssg
from string import ascii_uppercase as upp
import random

root = Tk()
root.title("Hangman")
root.iconbitmap('data\hm.ico')
root.resizable(0, 0)

wList = ["UMBRELLA", "WINDOW", "DESKTOP", "MIRROR", 'LEOPARD', 'PHOTOGRAPH',
         'MICROWAVE', 'ABYSS', 'BLIZZARD', 'WHICHCRAFT', 'ZOMBIE', 'FISHHOOK', 'OXYGEN']

img = [PhotoImage(file='data\hang0.png'),
       PhotoImage(file='data\hang1.png'),
       PhotoImage(file='data\hang2.png'),
       PhotoImage(file='data\hang3.png'),
       PhotoImage(file='data\hang4.png'),
       PhotoImage(file='data\hang5.png'),
       PhotoImage(file='data\hang6.png'),
       PhotoImage(file='data\hang7.png')]


def nGame():
    global word_s
    global nguess
    nguess = 0
    l1.config(image=img[0])
    wrd = random.choice(wList)
    word_s = " ".join(wrd)
    lblwrd.set(" ".join("_"*len(wrd)))


def guess(letter):
    global nguess
    if nguess < 7:
        txt = list(word_s)
        guessed = list(lblwrd.get())
        if (word_s.count(letter) > 0):
            for ch in range(len(txt)):
                if txt[ch] == letter:
                    guessed[ch] = letter
                lblwrd.set("".join(guessed))
            if lblwrd.get() == word_s:
                mssg.showinfo('Hangman', 'Congarts!!! You Guessed it!')
        else:
            nguess += 1
            l1.config(image=img[nguess])

    if nguess == 7:
        mssg.showwarning(
            'Hangman', 'Oh No! Better Luck Next Time! Game Over!!!')


l1 = Label(root, height=200, width=150)
l1.grid(row=1, column=0, columnspan=3, padx=10, pady=40)
l1.config(image=img[0])

lblwrd = StringVar()
Label(root, textvariable=lblwrd, font=('Roboto 25 bold')).grid(
    row=1, column=3, columnspan=6, padx=10)

a1 = Button(root, text='A', command=lambda: guess('A'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=0)
a2 = Button(root, text='B', command=lambda: guess('B'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=1)
a3 = Button(root, text='C', command=lambda: guess('C'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=2)
a4 = Button(root, text='D', command=lambda: guess('D'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=3)
a5 = Button(root, text='E', command=lambda: guess('E'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=4)
a6 = Button(root, text='F', command=lambda: guess('F'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=5)
a7 = Button(root, text='G', command=lambda: guess('G'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=6)
a8 = Button(root, text='H', command=lambda: guess('H'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=7)
a9 = Button(root, text='I', command=lambda: guess('I'), bg='black', fg='yellow',
            width=6, height=2, font=('Roboto 15 bold')).grid(row=2, column=8)

a11 = Button(root, text='J', command=lambda: guess('J'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=0)
a12 = Button(root, text='K', command=lambda: guess('K'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=1)
a13 = Button(root, text='L', command=lambda: guess('L'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=2)
a14 = Button(root, text='M', command=lambda: guess('M'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=3)
a15 = Button(root, text='N', command=lambda: guess('N'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=4)
a16 = Button(root, text='O', command=lambda: guess('O'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=5)
a17 = Button(root, text='P', command=lambda: guess('P'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=6)
a18 = Button(root, text='Q', command=lambda: guess('Q'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=7)
a19 = Button(root, text='R', command=lambda: guess('R'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=3, column=8)

a21 = Button(root, text='S', command=lambda: guess('S'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=0)
a22 = Button(root, text='T', command=lambda: guess('T'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=1)
a23 = Button(root, text='U', command=lambda: guess('U'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=2)
a24 = Button(root, text='V', command=lambda: guess('V'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=3)
a25 = Button(root, text='W', command=lambda: guess('W'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=4)
a26 = Button(root, text='X', command=lambda: guess('X'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=5)
a27 = Button(root, text='Y', command=lambda: guess('Y'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=6)
a28 = Button(root, text='Z', command=lambda: guess('Z'), bg='black', fg='yellow',
             width=6, height=2, font=('Roboto 15 bold')).grid(row=4, column=7)

a29 = Button(root, text='New\nGame', bg='yellow', fg='black', command=lambda: nGame(
), font=('Roboto 15 bold')).grid(row=4, column=8, sticky='NSWE')
"""
menu = Menu(root)
root.config(menu=menu)
opt = Menu(menu)
menu.add_cascade(label = 'Options',menu = opt)
opt.add_command(label="New Game",command=nGame())
opt.add_separator()
opt.add_command(label="Close Game",command=root.destroy)
"""
nGame()
root.mainloop()
