from tkinter import *
from PIL import ImageTk,Image
import random
import sys


name=str(input("Username:"))
print(f"Hello {name} and welcome to rock peper scissors game !")
max_win=int(input("enter the max:"))

#main window
root = Tk()
root.title("Rock Paper Scissors")
root.configure(background="black")
#images
rock_img= ImageTk.PhotoImage(Image.open("Rock.jpg"))
paper_img= ImageTk.PhotoImage(Image.open("paper.jpg"))
scissors_img= ImageTk.PhotoImage(Image.open("scissors.jpg"))
rock_img_pl2= ImageTk.PhotoImage(Image.open("Rock.jpg"))
paper_img_pl2= ImageTk.PhotoImage(Image.open("paper.jpg"))
scissors_img_pl2= ImageTk.PhotoImage(Image.open("scissors.jpg"))
ga_pic=ImageTk.PhotoImage(Image.open("gam.png"))



#insert pectures
pl1_label=Label(root,image=scissors_img,bg="gold")
pl2_label=Label(root,image=scissors_img_pl2,bg="gold")
pl2_label.grid(row=1,column=0)
pl1_label.grid(row=1,column=5)
game_label=Label(root,image=ga_pic,bg="gold")
game_label.grid(row=1,column=2)

# scores
pl1_Score=Label(root,text=0,font=('Arial',35),bg="black",fg="white")
pl2_Score=Label(root,text=0,font=('Arial',35),bg="black",fg="white")
word_score=Label(root,text="<= SCORE =>",font=100,bg="black",fg="white")
word_score.grid(row=2,column=2)
pl2_Score.grid(row=2,column=1)
pl1_Score.grid(row=2,column=3)

# indicator
pl1_indicator=Label(root,font=80,text=name.upper(),bg="black",fg="gold")
pl2_indicator=Label(root,font=80,text="COMPUTER",bg="black",fg="gold")
pl2_indicator.grid(row=1,column=1)
pl1_indicator.grid(row=1,column=3)

#message
msg = Label(root,font=50,bg="black",fg="red",text=f"start the game!! first to {max_win} wins (:")
msg.grid(row=4,column=2)

# change msg
def change_msg(x):
    msg['text'] = x

# change score player
def change_score_pl1():
    stop_game(int(pl1_Score["text"]))
    score1 = int(pl1_Score["text"])
    score1+=1
    pl1_Score["text"]=str(score1)
    if score1 == max_win and score1 > int(pl2_Score["text"]):
        change_msg(f"congraduation {name} ! You win the entire game ! ")
        score1=0
        pl1_Score["text"] = str(score1)
        pl2_Score["text"] = str(0)
    # stop_game(score1)


# change score player2
def change_score_pl2():
    stop_game(int(pl2_Score["text"]))
    score2 = int(pl2_Score["text"])
    score2+=1
    pl2_Score["text"]=str(score2)
    if score2 == max_win and score2 > int(pl1_Score["text"]):
        change_msg(f"congraduation cumputer ! You win the entire game ! ")
        score2=0
        pl2_Score["text"]=str(score2)
        pl1_Score["text"] = str(0)

    # stop_game(score2)

#the finish
def stop_game(x):
    if x == max_win+1:
        sys.exit()





#check the result
def check(player1,player2):
    if player1 == player2:
        change_msg(f"  its  a  draw in this round !!!     ")
    elif player1 =="rock":
        if player2 == "paper":
            change_msg(f"the computer wins this round!!!")
            change_score_pl2()
        else:
            change_msg(f"{name} the winer of this round!!!")
            change_score_pl1()
    elif player1=="paper":
        if player2 =="scissor":
            change_msg(f"the computer wines this round!!!")
            change_score_pl2()
        else:
            change_msg(f"{name} the winer of this round!!!")
            change_score_pl1()
    elif player1=="scissor":
        if player2 =="rock":
            change_msg(f"the computer wins this round!!!")
            change_score_pl2()
        else:
            change_msg(f"{name} the winer of this round!!!")
            change_score_pl1()
    elif int(pl2_Score["text"]) == max_win :
        if int(pl2_Score["text"])>int(pl1_Score["text"]):
            change_msg(f"congraduation computer ! You win the entire game ! ")
            stop_game(int(pl2_Score["text"]) == max_win,int(pl1_Score["text"]))
        else:
            quit()


    else:
        pass




#choices
choices=["rock","paper","scissor"]
def changechoice(x):
    # player2
    pl2_choices=random.choice(choices)
    if pl2_choices == "rock":
        pl2_label.configure(image=rock_img_pl2)
    elif pl2_choices=="paper":
        pl2_label.configure(image=paper_img_pl2)
    else:
        pl2_label.configure(image=scissors_img_pl2)

#player1
    if x=="rock":
        pl1_label.configure(image=rock_img)
    elif x=="paper":
        pl1_label.configure(image=paper_img)
    else:
        pl1_label.configure(image=scissors_img)

    check(x,pl2_choices)



#buttons
rock = Button(root,width=20,height=2,text="ROCK",bg="gold",fg="black",command=lambda :changechoice("rock")).grid(row=3,column=1)
paper = Button(root,width=20,height=2,text="PAPER",bg="gold",fg="black",command=lambda :changechoice("paper")).grid(row=3,column=2)
scissor = Button(root,width=20,height=2,text="SCISSOR",bg="gold",fg="black",command=lambda :changechoice("scissor")).grid(row=3,column=3)







root.mainloop()