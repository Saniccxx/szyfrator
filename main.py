import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("GUI")
        self.root.geometry("1280x720")
        self.label = tk.Label(self.root, text="Szyfrator", font=('Impact', 24))
        self.label.pack(padx = 10, pady = 30)
        self.textbox = tk.Text(self.root, height = 4, font=("Calibri", 16))
        self.textbox.place(x = 25, y = 100, height = 90, width = 500)
        self.select = tk.Button(self.root, text="Wybierz metodę", font=('Calibri', 24), command=self.select)
        self.select.place(x = 1000, y = 200, height = 50, width = 250)
        self.button = tk.Button(self.root, text = "Szyfruj!", font = ('Calibri', 24), command = self.get)
        self.button.place(x = 1000, y = 250, height = 50, width = 250)
        self.anwser = Label(self.root, text=None, font=('Impact', 24))
        self.anwser.place(x = 150, y = 400)


        self.options = ["Caesar", "Transposition cipher", "X"]

        # datatype of menu text
        self.clicked = tk.StringVar()
        print(self.clicked)

        # initial menu text
        self.clicked.set("Caesar")


        # Create Dropdown menu
        self.drop = OptionMenu(self.root, self.clicked, *self.options)
        self.drop.place(x=1050, y=100, width=150, height=30)


        self.root.mainloop()

    def get(self):
        if self.clicked.get() == "Caesar":
            print(self.textbox.get("1.0", tk.END))
            self.caesar()
        elif self.clicked.get() == "Transposition cipher":
            self.transposition_cipher()
        else:
            self.moja()

    def caesar(self):
        #65 90
        text = self.textbox.get("1.0", tk.END)
        if self.key.get() == "":
            key = 0
        else:
            key = int(self.key.get())
        cipher = ""
        text = text.upper()
        for letter in text:
            if letter == " ":
                cipher += " "
            elif 65 <= ord(letter) <= 90:
                code = ord(letter) - 65
                code = (code + key) % 26
                cipher += chr(code + 65)
        self.anwser.config(text=str(cipher))

        # return
    def moja(self):
        pass
    def select(self):
        if self.clicked.get() == "Caesar" or self.clicked.get() == "Transposition cipher":
            self.keylabel = Label(self.root, text="Klucz szyfrowania", font=('Impact', 21))
            self.keylabel.place(x = 1010, y = 330, height = 50, width = 200)
            current_value = tk.StringVar(value=0)
            self.key = ttk.Spinbox(
                self.root,
                from_=0,
                to=26,
                textvariable=current_value,
                wrap=True)
            self.key.place(x = 1060, y = 400, height = 25, width = 100)

        elif self.clicked.get() != "Caesar" or self.clicked.get() != "Transposition cipher":
            try:
                self.key.destroy()
                self.keylabel.destroy()
            except:
                pass

    def transposition_cipher(self):
        global key
        cipher = ""
        word = self.textbox.get("1.0", tk.END)
        word = word.upper()
        print(word)
        try:
            if self.key.get() == "":
                tk.messagebox.showinfo(title="Błąd", message="Wpisz odpowiedni klucz długością 5 symboli")
            elif len(str(self.key.get())) == 5:
                key = str(self.key.get())
                print(key)
            else:
                tk.messagebox.showinfo(title="Błąd", message="Wpisz odpowiedni klucz długością 5 symboli")
        except:
            tk.messagebox.showinfo(title="Błąd", message="Wpisz odpowiedni klucz długością 5 symboli")
        columns = 5
        rows = len(word) // columns
        if len(word) % columns > 0:
            rows += 1
        matrix = [[" " for c in range(columns)] for r in range(rows)]
        r = 0
        c = 0
        for letter in word:
            matrix[r][c] = letter
            c += 1
            if c == columns:
                c = 0
                r += 1
        first = 0
        for i in range(len(key)):
            column = int(key[first])
            for r in range(rows):
                cipher += matrix[r][column - 1]
            first += 1
            cipher += " "
        print(cipher)
        self.anwser.config(text=str(cipher))




gui=GUI()