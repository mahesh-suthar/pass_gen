import random
import string
from tkinter import *    #interface appear from this lib.
import pyperclip     
#it import the functionality  of copy in clipboard


def generator():
    small_alpha=string.ascii_lowercase
    capital_alpha=string.ascii_uppercase
    numbers=string.digits
    special_char=string.punctuation

    all=small_alpha+capital_alpha+numbers+special_char

    password_length=int(length_Box.get())
# radombly combine the input and create password as diffrent condition
    if choice.get()==1:
        passwordField.insert(0,random.sample(small_alpha+capital_alpha,password_length))
    if choice.get()==2:
        passwordField.insert(0,random.sample(small_alpha+capital_alpha+numbers,password_length))
    if choice.get()==3:
        passwordField.insert(0,random.sample(all,password_length))
    # password=random.sample(all,password_length)
    # passwordField.insert(0,password)

def copy():
    random_password=passwordField.get()
    pyperclip.copy(random_password)

root=Tk()

root.config(bg='gray20')
choice=IntVar()
Font=('arial',13,'bold')
passwordLabel=Label(root,text='Random Password Generator',font=('times new roman',20,'bold'),bg='gray20',fg='white')
passwordLabel.grid(pady=10)
weakradioButton=Radiobutton(root,text='Weak',value=1,variable=choice,font=Font)
weakradioButton.grid(pady=5)

mediumradioButton=Radiobutton(root,text='Medium',value=2,variable=choice,font=Font)
mediumradioButton.grid(pady=5)

strongradioButton=Radiobutton(root,text='Strong',value=3,variable=choice,font=Font)
strongradioButton.grid(pady=5)

lengthLabel=Label(root,text=' Password Length',font=('times new roman',17,'bold'),bg='gray20',fg='white')
lengthLabel.grid(pady=5)
length_Box=Spinbox(root,from_=8,to=18,width=8,font=Font)
length_Box.grid(pady=5)

generateradioButton=Radiobutton(root,text='Generate',font=Font,command=generator)
generateradioButton.grid(pady=5)

passwordField=Entry(root,width=30,bd=4,font=Font)
passwordField.grid(pady=5)
copyradioButton=Radiobutton(root,text='Copy',font=Font, command=copy)
copyradioButton.grid(pady=8)

developerLabel=Label(root,text=' By Kunal Singh ',font=('times new roman',14,'bold'),bg='gray20',fg='white')
developerLabel.grid(pady=5)
root.mainloop()
