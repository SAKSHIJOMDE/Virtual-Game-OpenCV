from tkinter import *
from tkinter import messagebox
from PIL import ImageTk


def play_page():
    play.destroy()
    import signin


play=Tk()
play.title('VARTUAL QUEZE GAME')
play.resizable(False,False)

background=ImageTk.PhotoImage(file='VartualQueze.png')

bgLabel=Label(play,image=background)
bgLabel.grid()

frame=Frame(play,bg='white')
frame.place(x=554,y=100)

playButton=Button(play,text='PLAY',font=('Open sans',20,'bold'),fg='gold1',
                   bg='deeppink1',activeforeground='blue',activebackground='white',cursor='hand2',bd=0,
                   command=play_page)
playButton.place(x=220,y=400)


play.mainloop()