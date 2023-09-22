from tkinter import *
import os
import sys


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS2
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


root = Tk()
root.geometry("800x600")
root.configure(bg='#efe7c8')
root.resizable(0, 0)
root.title('Arcade Game Box')
root.iconbitmap(resource_path('data\icon.ico'))

l1 = Label(root)
l1.config(text='\nArcade Game Box', justify='center',
          font=('Cambria 30 bold'), fg='black', bg='#efe7c8')
l1.pack()

l2 = Label(root)
l2.config(text='\nGames :', justify='center', font=(
    'Cambria 25 bold'), fg='red', bg='#efe7c8')
l2.pack()


def selGam1():
    os.system(f'python "{resource_path("src/TicTacToe.py")}"')


def selGam2():
    os.system(f'python "{resource_path("src/Hangman2_MP.py")}"')


def selGam3():
    os.system(f'python "{resource_path("src/Pong.py")}"')


f1 = Frame(root, bg='#efe7c8')
f1.pack()

i1 = PhotoImage(file=resource_path("data/ttt.png"))
i2 = PhotoImage(file=resource_path("data/hangman.png"))
i3 = PhotoImage(file=resource_path("data/pong.png"))


b1 = Button(f1, image=i1, height=150, width=150, command=selGam1,
            relief='solid').grid(row=1, column=0, padx=50, pady=30)
b2 = Button(f1, image=i2, height=150, width=150, command=selGam2,
            relief='solid').grid(row=1, column=1, padx=50, pady=30)
b3 = Button(f1, image=i3, height=150, width=150, command=selGam3,
            relief='solid').grid(row=1, column=2, padx=50, pady=30)


t1 = Button(f1, text='Tic-Tac-Toe', command=selGam1, font=('Arial 20 bold'),
            relief='solid', bg='#efe7c8', fg='blue').grid(row=2, column=0, padx=50, pady=30)
t2 = Button(f1, text='Hangman', command=selGam2, font=('Arial 20 bold'),
            relief='solid', bg='#efe7c8', fg='blue').grid(row=2, column=1, padx=50, pady=30)
t2 = Button(f1, text='2P Ping-Pong', command=selGam3, font=('Arial 20 bold'),
            relief='solid', bg='#efe7c8', fg='blue').grid(row=2, column=2, padx=50, pady=30)


root.mainloop()
