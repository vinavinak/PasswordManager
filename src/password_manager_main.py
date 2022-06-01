#!/usr/bin/env python3  
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
# Created By  : Kana Kunikata
# Created Date: 02/04/2022
# version ='1.0'
# ---------------------------------------------------------------------------

""" The implementation of Password Manager """

from tkinter import *
import tkinter.font as font
from tkinter import messagebox
import pyperclip
import random

DEFAULT_EMAIL = "xxx@xxx.com"
APP_LOGO = 'logo2.png'
MY_SECRETS = 'my_password.txt'

class PasswordManager:

# ---------------------------- UI SETUP ------------------------------- #

    def __init__(self, master):
        self.master = master
        self.master.title("Password Manager")
        self.master.config(padx=50, pady=50)

        # Font
        self.my_font = font.Font(size=10)

        #Image by Canvas
        self.canvas = Canvas(self.master, height=200, width=200)
        self.logo_img = PhotoImage(file=APP_LOGO)
        self.canvas.create_image(100,100,image=self.logo_img)
        self.canvas.grid(row=0,column=1)

        #Labels
        self.website_label = Label(text="Website:")
        self.website_label.grid(row=1)
        self.email_label = Label(text="Email/Username:")
        self.email_label.grid(row=2)
        self.password_label = Label(text="Password:")
        self.password_label.grid(row=3)

        #Entries
        self.website_entry = Entry(width=35)
        self.website_entry.grid(row=1,column=1,columnspan=2)
        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2,column=1,columnspan=2)
        self.email_entry.insert(0,DEFAULT_EMAIL)
        self.password_entry = Entry(width=24)
        self.password_entry.grid(row=3,column=1,sticky=E)

        #Buttons
        self.generate_password_button = Button(text="Generate Password",width=13,command=self.generate_password)
        self.generate_password_button.grid(row=3,column=2,sticky=W)
        self.generate_password_button['font'] = self.my_font
        self.add_button = Button(text="Add",width=36,command=self.save)
        self.add_button.grid(row=4,column=1,columnspan=2)

# ---------------------------- SAVE PASSWORD ------------------------------- #

    def save(self):
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        if len(website) == 0 or len(password) == 0:
            messagebox.showinfo(title="Oops",message="Please make sure you hav't left any fields empty")
        else:
            if_ok = messagebox.askokcancel(title=website, message=f"these are the default enttered:" 
            f"\nEmail: {email} \nPassword: {password} \nis it okat to save?")

            if if_ok:
                with open(MY_SECRETS,'a') as data_file:
                    data_file.write(f"{website} | {email} | {password}\n")
                    self.website_entry.delete(0, END)
                    self.password_entry.delete(0, END)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
    def generate_password(self):
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = []

        paasword_letters = [random.choice(letters) for _ in range(nr_letters) ]
        paasword_symbols = [random.choice(symbols) for _ in range(nr_symbols) ]
        paasword_numbers = [random.choice(numbers) for _ in range(nr_numbers) ]

        password_list = paasword_letters + paasword_symbols + paasword_numbers

        random.shuffle(password_list)

        password = "".join(password_list)
        self.password_entry.insert(0, password)
        pyperclip.copy(password)

        #print(f"Your password is: {password}")

def main(): 
    root = Tk()
    pm_app = PasswordManager(root)
    #root.mainloop()
    return root

if __name__ == '__main__':
    main().mainloop()




