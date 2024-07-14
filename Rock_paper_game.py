import tkinter as tk
import random
from tkinter import messagebox

def winner(user_c,computer_c):
    if (user_c==computer_c):
        return "It's a tie"
    elif(user_c=='rock' and computer_c=='scissor')or(user_c=='paper' and computer_c=='rock')or(user_c=='scissor'and computer_c=='paper'):
        return "You win!"
    else:
        return "Computer win!"
def play_score(user_c):
    global user_sc,computer_sc
    computer_c=random.choice(['rock','paper','scissor'])
    result=winner(user_c,computer_c)
    if "You win!" in result:
        user_sc=user_sc+1
    elif "Computer win!" in result:
        computer_sc=computer_sc+1
    result_label.config(text=f"Your choice: {user_c}\nComputer's choice: {computer_c}\n{result}")
    score_label.config(text=f"Your Score: {user_sc} | Computer Score: {computer_sc}")

def quits():
    ask = messagebox.askokcancel("Quit/Play","Do you want to quit?")
    if (ask==True):
        root.quit()
    else:
        play_score()

root = tk.Tk()

root.geometry('400x350')
root.resizable(False,False)
root.title("Rock Paper Scissor Game")
user_sc=0
computer_sc=0

bar = tk.Frame(root, bg="teal", height=50)
bar.pack(fill=tk.X)

text = tk.Label(bar, text="Rock Paper Scissor Game", bg='teal', font=('arial', 16, 'bold'), fg='white')
text.pack(pady=6)

buttons_frame = tk.Frame(root, bg='white')
buttons_frame.pack(pady=15)

rock_button = tk.Button(buttons_frame, text="Rock", width=10, command=lambda:play_score("rock"), background="teal", fg="white", borderwidth=3)
rock_button.grid(row=0, column=0, padx=5, pady=5)

paper_button = tk.Button(buttons_frame, text="Paper", width=10, command=lambda:play_score("paper"), background="teal", fg="white", borderwidth=3)
paper_button.grid(row=0, column=1, padx=5, pady=5)

scissor_button = tk.Button(buttons_frame, text="Paper", width=10, command=lambda:play_score("scissor"), background="teal", fg="white", borderwidth=3)
scissor_button.grid(row=0, column=2, padx=5, pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=20)

score_label = tk.Label(root, text=f"Your Score: {user_sc} | Computer Score: {computer_sc}", font=("Arial", 14))
score_label.pack(pady=10)

quit_button = tk.Button(root, text="Quit", width=10, command=quits, background="teal", fg="white", borderwidth=3)
quit_button.pack()

root.mainloop()