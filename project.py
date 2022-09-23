#!/usr/bin/python3

import random
from tkinter import *


root = Tk()
root.geometry("350x400")
root.title("Rock/Paper/Scissors Game")

# label widgets
label_a = Label(root, 
    text="Welcome to my game!",
    fg="white",   # set the text color
    bg="navy",   # set the background color
    width=50,   # in text units
    height=3,   # in text units
    font="Times 12 bold", # set the font
)

label_b = Label(root, 
    text="Are you ready?",
    fg="black",
    font="Times 12 bold",
)
label_a.pack()
label_b.pack()

# global variables, changed during game
player_score = 0
ai_score = 0
player_pick = ''
ai_pick = ''

# import images
# images source: https://www.coltnews.com/wp-content/uploads/2016/04/RPS.png
images_list = [
    PhotoImage(file='images/r.png'),
    PhotoImage(file='images/p.png'),
    PhotoImage(file='images/s.png')
]

#creates a file for result and save them in every game
def save_file(x):
    f=open("result.txt","a")
    f.write(str(x))
    f.close()
    

# main part of code, top level
def game():
    save_file("------New Game------\n") #add label of New Game to the result file every time you press "New Game button"
    
    game = Toplevel(root) # open in new window
    game.geometry("350x400") 

# make everything centered
    game.columnconfigure(0, weight=1)
    game.rowconfigure(0, weight=1)

# main frame
    frame= Frame(game, bg="grey")
    frame.grid()

    title1 = Label(frame, text="Welcome to my game!", bg="#66CDAA",fg="black", relief=RAISED, bd=5, font="Times 12 bold")   # a label widget
    title1.grid(column=0, row=0, columnspan=3, sticky=NSEW)

    title2 = Label(frame, text="Let's play!", bg="#66CDAA", fg="black", relief=SUNKEN, bd=5, font="Times 12 bold")   # a label widget
    title2.grid(column=0, row=1, columnspan=3, sticky=NSEW)

    window = Label(frame, height=12, width=30, bg="#66CDAA", relief=SUNKEN, bd=5)
    window.grid(column=0,row=3, columnspan=3, sticky=NSEW)


    def ai_choice():
        return random.choice(['rock','paper','scissor']) 

    def rock():
        global player_pick
        global ai_pick
        global player_score
        global ai_score
        player_pick='rock'
        ai_pick=ai_choice()
        if ai_pick == str('scissor'):
            print("You win")
            player_score+=1
        elif ai_pick == str('paper'):
            print("You lose")
            ai_score+=1
        else:
            print("Tie")
        text = Text(frame, height=12, width=22, bg="#66CDAA")
        text.grid(column=0, row=3, columnspan=3)
        result = "Your Choice: {} \nAI's Choice: {} \nYour Score: {} \nAI Score: {} \n".format(player_pick,ai_pick,player_score, ai_score)     
        text.insert(END,result)
        save_file(result)

    def paper():
        global player_pick
        global ai_pick
        global player_score
        global ai_score
        player_pick='paper'
        ai_pick=ai_choice()
        if ai_pick == str('rock'):
            print("You win")
            player_score+=1
        elif ai_pick == str('scissor'):
            print("You lose")
            ai_score+=1
        else:
            print("Tie")
        text = Text(frame, height=12, width=22, bg='#66CDAA')
        text.grid(column=0, row=3, columnspan=3)
        result = "Your Choice: {} \nAI's Choice: {} \nYour Score: {} \nAI Score: {} \n".format(player_pick,ai_pick,player_score, ai_score)    
        text.insert(END,result)
        save_file(result)

    def scissor():
        global player_pick
        global ai_pick
        global player_score
        global ai_score
        player_pick='scissor'
        ai_pick=ai_choice()
        if ai_pick == str('paper'):
            print("You win")
            player_score+=1
        elif ai_pick == str('rock'):
            print("You lose")
            ai_score+=1
        else:
            print("Tie")
        text = Text(frame, height=12, width=22, bg="#66CDAA")
        text.grid(column=0, row=3, columnspan=3)
        result = "Your Choice: {} \nAI's Choice: {} \nYour Score: {} \nAI Score: {} \n".format(player_pick,ai_pick,player_score, ai_score)    
        text.insert(END,result)
        save_file(result)



    button1 = Button(frame, bg="orange", image=images_list[0], relief=RAISED, bd=5, command=rock)
    button1.grid(column=0,row=2, sticky=NSEW)
    button2 = Button(frame, bg="#DC143C", image=images_list[1], relief=RAISED, bd=5, command=paper)
    button2.grid(column=1,row=2, sticky=NSEW)
    button3 = Button(frame, bg="green", image=images_list[2], relief=RAISED, bd=5, command=scissor)
    button3.grid(column=2,row=2, sticky=NSEW)

    button4 = Button(frame, bg="red", text="Quit", relief=RAISED, bd=5, command=game.destroy)
    button4.grid(column=0,row=4, columnspan=3, sticky=NSEW)


# wigets for main window
frame_a = Frame(root, # the first argument
    bg="black",   # set the background color to black
    width=50,   # in pixels
    height=30,   # in pixels
    relief=RAISED,   # border decoration
    bd=5,
)
frame_a.pack()

button = Button(frame_a,
    text="New game",
    width=25,
    height=5,
    bg="navy",
    fg="white",
    font="Times 12 bold",
    command=game,
)
button.pack()

button = Button(frame_a,
    text="Quit",
    width=25,
    height=5,
    bg="navy",
    fg="white",
    font="Times 12 bold",
    command=root.quit,
)
button.pack()


root.mainloop()

