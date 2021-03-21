import requests
from tkinter import *
from PIL import ImageTk, Image  
import time
import random
import os


#random paragraphs
paragraphs = ["Spending time at national parks can be an exciting adventure, but this wasn't the type of excitement she was hoping to experience. As she contemplated the situation she found herself in, she knew she'd gotten herself in a little more than she bargained for. It wasn't often that she found herself in a tree staring down at a pack of wolves that were looking to make her their next meal.","There was something beautiful in his hate. It wasn't the hate itself as it was a disgusting display of racism and intolerance. It was what propelled the hate and the fact that although he had this hate, he didn't understand where it came from. It was at that moment that she realized that there was hope in changing him.","He sat staring at the person in the train stopped at the station going in the opposite direction. She sat staring ahead, never noticing that she was being watched. Both trains began to move and he knew that in another timeline or in another universe, they had been happy together.","If you can imagine a furry humanoid seven feet tall, with the face of an intelligent gorilla and the braincase of a man, you'll have a rough idea of what they looked like -- except for their teeth. The canines would have fitted better in the face of a tiger, and showed at the corners of their wide, thin-lipped mouths, giving them an expression of ferocity.","The shoes had been there for as long as anyone could remember. In fact, it was difficult for anyone to come up with a date they had first appeared. It had seemed they'd always been there and yet they seemed so out of place.","He walked down the steps from the train station in a bit of a hurry knowing the secrets in the briefcase must be secured as quickly as possible. Bounding down the steps, he heard something behind him and quickly turned in a panic","There was something beautiful in his hate. It wasn't the hate itself as it was a disgusting display of racism and intolerance. It was what propelled the hate and the fact that although he had this hate, he didn't understand where it came from. It was at that moment that she realized that there was hope in changing him","I'm going to hire professional help tomorrow. I can't handle this anymore. She fell over the coffee table and now there is blood in her catheter. This is much more than I ever signed up to do","What is the best way to get what you want? she asked. He looked down at the ground knowing that she wouldn\'t like his answer. He hesitated, knowing that the truth would only hurt. How was he going to tell her that the best way for him to get what he wanted was to leave her","The wolves stopped in their tracks, sizing up the mother and her cubs. It had been over a week since their last meal and they were getting desperate. The cubs would make a good meal","She reached her goal, exhausted. Even more chilling to her was that the euphoria that she thought she'd feel upon reaching it wasn't there. Something wasn't right. Was this the only feeling she'd have for over five years of hard work?"]
#create main window
root = Tk()
root.title("Typing Test")
root.geometry("800x550")

#expand root window
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

#frame1
frame1 = Frame(root, bg="red")

#frame 1 content
welcome_lbl =  Label(frame1, text='', font='times 35')
#frame 1 set background
path = f"{os.path.dirname(os.path.realpath(__file__))}\\typing.png"
stgImg = PhotoImage(file=path)
welcome_lbl.configure(image=stgImg)
welcome_lbl.image = stgImg
welcome_lbl.pack(fill='both', expand=True)

#start button
start_btn = Button(frame1, text='Start',command=lambda:show_frame(frame2), font=("Times New Roman", 15, "bold"), bg="gray")
start_btn.pack(fill='x', ipady=15)



#frame 2 
frame2 = Frame(root, bg="midnight blue")

#frame 2 content
text_to_copy = Label(frame2, text=f'{random.choice(paragraphs)}', font=('bold', 15), height=6,wraplength=700)
text_to_copy.pack(fill = BOTH, pady=30)

#text to be typed

test_input = Entry(frame2, text='', width=40, font=('Helvetica', 15))
test_input.pack(fill = BOTH, pady=30, ipady=42)
t0 = 0
t1 = 0
test_input.bind("<Key>", lambda event, arg=(0):start_timer())
test_input.bind('<Return>', (lambda event: show_result()))


score_lbl = Label(frame2, text='Score : ', font=('bold', 15), bg="red", width=30)
score_lbl.pack(anchor="e")

def start_timer():
    global t0
    if t0 == 0 : t0 = time.time()
def show_result():
    global t0,t1, score_lbl, test_input, text_to_copy
    number_of_words = len([word for word in test_input.get().split()])
    t1 = time.time()
    score_lbl['text'] = f"Score : {round((60 * number_of_words) / round(round(t1-t0, 2) , 2))}word(s)/minute"
    test_input.delete(0, 'end')
    text_to_copy['text'] = random.choice(paragraphs)
    t0 = 0
    t1 = 0
    




    
c_window_size = root.winfo_reqwidth()

#exit button
exit_btn = Button(frame2, text='exit',command=root.destroy, width=10, height=2, font='bold 15')
exit_btn.pack(padx=c_window_size/3, pady=10, side=LEFT)

#back button
back_btn = Button(frame2, text='back',command=lambda:show_frame(frame1), width=10, height=2, font='bold 15')
back_btn.pack(padx=c_window_size/3, pady=10, side=LEFT)




for frame in (frame2, frame1):
    frame.grid(row=0,column=0,sticky='nsew')
frame1.tkraise()


def show_frame(frame):
    frame.tkraise()
    test_input.delete(0, 'end')
    text_to_copy['text'] = random.choice(paragraphs)
    t0 = 0
    t1 = 0
    score_lbl['text'] = "Score : "





root.mainloop()