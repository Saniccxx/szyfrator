import tkinter as tk
import aspose.pdf as ap
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Szyfrator")
        self.root.geometry("1280x720")
        self.root.configure(bg='beige')
        self.label = tk.Label(self.root, text="Szyfrator", font=('Impact', 32), bg='beige')
        self.label.pack(padx = 10, pady = 30)
        self.textbox = tk.Text(self.root, height = 4, font=("Calibri", 16))
        self.textbox.place(x = 25, y = 100, height = 130, width = 500)
        self.select = tk.Button(self.root, text="Wybierz metodę", font=('Calibri', 24), command=self.select)
        self.select.place(x = 1000, y = 200, height = 50, width = 250)
        self.button = tk.Button(self.root, text = "Szyfruj!", font = ('Calibri', 24), command = self.get)
        self.button.place(x = 1000, y = 250, height = 50, width = 250)
        self.anwser = tk.Label(self.root, wraplength=600, text=None, font=('Impact', 24), bg='beige')
        self.anwser.place(x = 150, y = 400)
        self.info = tk.Button(self.root, text = "Jak to działa?", font = ('Calibri', 24, "bold"), command = self.help)
        self.info.place(x = 25, y = 25, height = 50, width = 250)
        self.export = tk.Button(self.root, text="Eksportować w PDF", font=('Calibri', 24), command=self.pdf)
        self.export.place(x = 950, y = 630, height = 65, width = 300)
        self.options = ["Caesar Cipher", "Transposition Cipher", "Cyrillic Cipher"]
        self.clicked = tk.StringVar()
        print(self.clicked)
        self.clicked.set("Caesar Cipher")


        self.drop = OptionMenu(self.root, self.clicked, *self.options)
        self.drop.place(x=1050, y=100, width=150, height=30)


        self.root.mainloop()

    def get(self):
        if self.clicked.get() == "Caesar Cipher":
            print(self.textbox.get("1.0", tk.END))
            self.caesar()
        elif self.clicked.get() == "Transposition Cipher":
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
        word = self.textbox.get("1.0", tk.END)
        cipher = ""
        word = word.upper()
        for letter in word:
            if letter == "A":
                cipher += "А"
            elif letter == "B":
                cipher += "Б"
            elif letter == "C":
                cipher += "Ц"
            elif letter == "D":
                cipher += "Д"
            elif letter == "E":
                cipher += "Е"
            elif letter == "F":
                cipher += "Ф"
            elif letter == "G":
                cipher += "Г"
            elif letter == "H":
                cipher += "Х"
            elif letter == "I":
                cipher += "І"
            elif letter == "J":
                cipher += "Й"
            elif letter == "K":
                cipher += "К"
            elif letter == "L":
                cipher += "Л"
            elif letter == "M":
                cipher += "М"
            elif letter == "N":
                cipher += "Н"
            elif letter == "O":
                cipher += "О"
            elif letter == "P":
                cipher += "П"
            elif letter == "Q":
                cipher += "-к'ю-"
            elif letter == "R":
                cipher += "Р"
            elif letter == "S":
                cipher += "С"
            elif letter == "T":
                cipher += "Т"
            elif letter == "U":
                cipher += "У"
            elif letter == "V":
                cipher += "В"
            elif letter == "W":
                cipher += "В"
            elif letter == "X":
                cipher += "-ікс-"
            elif letter == "Y":
                cipher += "И"
            elif letter == "Z":
                cipher += "З"
            else:
                cipher += letter
        self.anwser.config(text=str(cipher))

    def select(self):
        self.anwser.config(text="")

        if self.clicked.get() == "Transposition Cipher":
            try:
                self.key.destroy()
            except:
                print("")
            try:
                self.keylabel.destroy()
            except:
                print("")
            try:
                self.dlugosclabel.destroy()
            except:
                print("")
            self.keylabel = tk.Label(self.root, text="Klucz szyfrowania", font=('Impact', 21), bg='beige')
            self.keylabel.place(x=1010, y=330, height=50, width=200)
            current_value = tk.StringVar(value=0)
            self.key = ttk.Spinbox(
                self.root,
                from_=0,
                to=26,
                textvariable=current_value,
                wrap=True)

            self.key.place(x=1060, y=400, height=25, width=100)
            self.dlugosclabel = tk.Label(self.root, text="Wpisz klucz długością 5 cyfr od 1 do 5 (na przyklad: 54123)", wraplength=200, font=('Impact', 21), bg='beige')
            self.dlugosclabel.place(x = 1010, y = 450, height = 150, width = 200)

        elif self.clicked.get() == "Caesar Cipher":
            try:
                self.key.destroy()
            except:
                print("")
            try:
                self.keylabel.destroy()
            except:
                print("")
            try:
                self.dlugosclabel.destroy()
            except:
                print("")
            self.keylabel = tk.Label(self.root, text="Klucz szyfrowania", font=('Impact', 21), bg='beige')
            self.keylabel.place(x = 1010, y = 330, height = 50, width = 200)
            current_value = tk.StringVar(value=0)
            self.key = ttk.Spinbox(
                self.root,
                from_=0,
                to=26,
                textvariable=current_value,
                wrap=True)
            self.key.place(x = 1060, y = 400, height = 25, width = 100)
            try:
                self.dlugosclabel.destroy()
            except:
                print("")
        else:
            try:
                self.key.destroy()
            except:
                print("")
            try:
                self.keylabel.destroy()
            except:
                print("")
            try:
                self.dlugosclabel.destroy()
            except:
                print("")

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


    def pdf(self):
        file = open("index.txt", "r")
        l = None
        for line in file:
            l = line
        self.i = (int(l) + 1)
        file = open("index.txt", "w")
        # file.truncate(0)
        wr = str(self.i)
        file.write(wr)
        try:
            self.document = ap.Document(f"{self.i}.pdf")
        except:
            self.document = ap.Document()

        self.page = self.document.pages.add()
        fragment = ap.text.TextFragment(self.anwser.cget("text"))
        self.page.paragraphs.add(fragment)
        self.document.save(f"{self.i}.pdf")
    def help(self):
        tk.messagebox.showinfo(title="Informacja", message="Żeby wybrać metodę szyfrowania wybiesz metodę z listy i naciśnij Wybierz metodę. "
                                                           "By zaszyfrować twój tekst naciśnij Szyfruj! "
                                                           "Caesar Cipher - przesuwa literki alfabetycznie o klucz. Transposition Cypher - wpisuje tekst w listę i wczytuje go według klucza(np. 51423)."
                                                           " Cyryllic Cipher - przekształca tekst na cyryliczny rodzaj pisma. "
                                                           "Plik PDF NIE jest edytowany, każdy kolejny eksport zapisuje tekst w nowym pliku PDF")

gui=GUI()
