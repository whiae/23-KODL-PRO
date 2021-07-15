from tkinter import *
from tkinter import messagebox


def akcjaAutor():
    messagebox.showinfo("Autor", "Weronika Szczegodzińska\nKognitywistyka, semestr I")

def akcjaPrzycisk():
    if (wartosc.get() == 1 and wartosc1.get() == 5 and wartosc2.get() == 9):
        messagebox.showinfo("Wynik","Twój wynik to: 3 punkty")
    elif (wartosc.get() == 1 and wartosc1.get() == 5 and wartosc2.get() != 9)\
            or (wartosc.get() == 1 and wartosc1.get() != 5 and wartosc2.get() == 9)\
            or (wartosc.get() != 1 and wartosc1.get() == 5 and wartosc2.get() == 9):
        messagebox.showinfo("Wynik", "Twój wynik to: 2 punkty")
    elif (wartosc.get() == 1 and wartosc1.get() != 5 and wartosc2.get() != 9)\
            or (wartosc.get() != 1 and wartosc1.get() == 5 and wartosc2.get() != 9)\
            or (wartosc.get() != 1 and wartosc1.get() != 5 and wartosc2.get() == 9):
        messagebox.showinfo("Wynik", "Twój wynik to: 1 punkt")
    else:
        messagebox.showinfo("Wynik", "Twój wynik to: 0 punktów")

mainWindow = Tk()
menuBar = Menu(mainWindow)
wartosc = IntVar()
wartosc1 = IntVar()
wartosc2 = IntVar()

firstMenu = Menu(menuBar, tearoff = 0)
firstMenu.add_command(label="Autor", command=akcjaAutor)
firstMenu.add_command(label="Wyjdź", command=mainWindow.quit)
menuBar.add_cascade(label="Info", menu=firstMenu)

label_1 = Label(mainWindow, text="Pierwszy dzień tygodnia to:").pack()
Odpowiedz_1 = Radiobutton(mainWindow,text="Poniedziałek", variable = wartosc, value = 1).pack()
Odpowiedz_2 = Radiobutton(mainWindow,text="Wtorek", variable = wartosc, value = 2).pack()
Odpowiedz_3 = Radiobutton(mainWindow,text="Środa", variable = wartosc, value = 3).pack()

label_2 = Label(mainWindow, text="Drugi dzień tygodnia to:").pack()
Odpowiedz_4 = Radiobutton(mainWindow,text="Poniedziałek", variable = wartosc1, value = 4).pack()
Odpowiedz_5 = Radiobutton(mainWindow,text="Wtorek", variable = wartosc1, value = 5).pack()
Odpowiedz_6 = Radiobutton(mainWindow,text="Środa", variable = wartosc1, value = 6).pack()

label_3 = Label(mainWindow, text="Trzeci dzień tygodnia to:").pack()
Odpowiedz_7 = Radiobutton(mainWindow,text="Poniedziałek", variable = wartosc2, value = 7).pack()
Odpowiedz_8 = Radiobutton(mainWindow,text="Wtorek", variable = wartosc2, value = 8).pack()
Odpowiedz_9 = Radiobutton(mainWindow,text="Środa", variable = wartosc2, value = 9).pack()


przycisk1 = Button(mainWindow, text="Wyślij", command=akcjaPrzycisk)
przycisk1.pack(side=BOTTOM)

mainWindow.config(menu = menuBar)
mainWindow.mainloop()