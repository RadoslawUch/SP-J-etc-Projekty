import tkinter as tk
import random
import time
from tkinter import messagebox

POZIOMY = {
    "Łatwy": (9, 9, 10),
    "Normalny": (12, 20, 35),
    "Trudny": (16, 30, 100)
}

class Saper:
    def __init__(self, root):
        self.root = root
        self.root.title("saper")
        self.root.configure(bg="#d9d9d9")
        
        self.ustawienia = POZIOMY["Trudny"]
        self.wiersze, self.kolumny, self.liczba_min = self.ustawienia
        
        self.miny = set()
        self.flagi = set()
        self.odkryte = set()
        self.koniec_gry = False
        self.czas_startu = None
        self.id_stopera = None
        
        self.stworz_menu()
        self.stworz_interfejs()
        self.nowa_gra()

    def stworz_menu(self):
        pasek_menu = tk.Menu(self.root)
        self.root.config(menu=pasek_menu)
        menu_gry = tk.Menu(pasek_menu, tearoff=0)
        pasek_menu.add_cascade(label="Poziom trudności", menu=menu_gry)
        for nazwa in POZIOMY.keys():
            menu_gry.add_command(label=nazwa, command=lambda n=nazwa: self.zmien_poziom(n))

    def zmien_poziom(self, nazwa):
        if self.id_stopera:
            self.root.after_cancel(self.id_stopera)
        self.ustawienia = POZIOMY[nazwa]
        self.wiersze, self.kolumny, self.liczba_min = self.ustawienia
        self.ramka_planszy.destroy()
        self.panel_gorny.destroy()
        self.stworz_interfejs()
        self.nowa_gra()

    def stworz_interfejs(self):
        self.panel_gorny = tk.Frame(self.root, bg="#d9d9d9", pady=10)
        self.panel_gorny.pack(fill="x")

        self.etykieta_min = tk.Label(self.panel_gorny, text="0000", font=("Courier", 30, "bold"), 
                                    bg="black", fg="red", width=5)
        self.etykieta_min.pack(side="left", padx=20)

        self.przycisk_reset = tk.Button(self.panel_gorny, text="🙂", font=("Arial", 20), 
                                        command=self.nowa_gra, bg="#d9d9d9", width=3)
        self.przycisk_reset.pack(side="left", expand=True)

        self.etykieta_czasu = tk.Label(self.panel_gorny, text="0000", font=("Courier", 30, "bold"), 
                                      bg="black", fg="red", width=5)
        self.etykieta_czasu.pack(side="right", padx=20)

        self.ramka_planszy = tk.Frame(self.root, bd=3, relief="sunken")
        self.ramka_planszy.pack(padx=10, pady=10)

        self.przyciski = []
        for r in range(self.wiersze):
            wiersz_przyciskow = []
            for c in range(self.kolumny):
                btn = tk.Button(self.ramka_planszy, width=2, height=1, font=("Arial", 9, "bold"),
                                relief="raised", bg="#d9d9d9",
                                command=lambda r=r, c=c: self.klikniecie(r, c))
                btn.bind("<Button-3>", lambda e, r=r, c=c: self.postaw_flage(r, c))
                btn.grid(row=r, column=c)
                wiersz_przyciskow.append(btn)
            self.przyciski.append(wiersz_przyciskow)

    def aktualizuj_stoper(self):
        if self.czas_startu and not self.koniec_gry:
            sekundy = int(time.time() - self.czas_startu)
            self.etykieta_czasu.config(text=f"{min(sekundy, 9999):04d}")
            self.id_stopera = self.root.after(1000, self.aktualizuj_stoper)

    def nowa_gra(self):
        if self.id_stopera:
            self.root.after_cancel(self.id_stopera)
        self.miny.clear()
        self.flagi.clear()
        self.odkryte.clear()
        self.koniec_gry = False
        self.czas_startu = None
        self.przycisk_reset.config(text="🙂")
        self.etykieta_min.config(text=f"{self.liczba_min:04d}")
        self.etykieta_czasu.config(text="0000")
        
        pozycje = [(r, c) for r in range(self.wiersze) for c in range(self.kolumny)]
        self.miny = set(random.sample(pozycje, self.liczba_min))

        for r in range(self.wiersze):
            for c in range(self.kolumny):
                self.przyciski[r][c].config(text="", bg="#d9d9d9", relief="raised", state="normal")

    def klikniecie(self, r, c):
        if self.koniec_gry or (r, c) in self.flagi or (r, c) in self.odkryte:
            return
        
        if self.czas_startu is None:
            self.czas_startu = time.time()
            self.aktualizuj_stoper()

        if (r, c) in self.miny:
            self.przegrana()
        else:
            self.odkryj_pole(r, c)
            if len(self.odkryte) == (self.wiersze * self.kolumny) - self.liczba_min:
                self.wygrana()

    def odkryj_pole(self, r, c):
        if (r, c) in self.odkryte or (r, c) in self.flagi: return
        self.odkryte.add((r, c))
        liczba = self.policz_sasiadow(r, c)
        self.przyciski[r][c].config(relief="flat", bg="#bdbdbd", state="disabled")
        kolory = ["", "blue", "green", "red", "darkblue", "darkred", "cyan", "black", "gray"]
        if liczba > 0:
            self.przyciski[r][c].config(text=str(liczba), disabledforeground=kolory[liczba])
        else:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.wiersze and 0 <= nc < self.kolumny:
                        self.odkryj_pole(nr, nc)

    def postaw_flage(self, r, c):
        if self.koniec_gry or (r, c) in self.odkryte: return
        if (r, c) in self.flagi:
            self.flagi.remove((r, c))
            self.przyciski[r][c].config(text="", fg="black")
        else:
            self.flagi.add((r, c))
            self.przyciski[r][c].config(text="🚩", fg="red")
        pozostalo = self.liczba_min - len(self.flagi)
        self.etykieta_min.config(text=f"{max(0, pozostalo):04d}")

    def policz_sasiadow(self, r, c):
        licznik = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if (r + dr, c + dc) in self.miny:
                    licznik += 1
        return licznik

    def przegrana(self):
        self.koniec_gry = True
        self.przycisk_reset.config(text="😵")
        for (r, c) in self.miny:
            self.przyciski[r][c].config(text="💣", bg="red")

    def wygrana(self):
        self.koniec_gry = True
        self.przycisk_reset.config(text="😎")
        messagebox.showinfo("Gratulacje", "Wygrałeś!")

if __name__ == "__main__":
    root = tk.Tk()
    gra = Saper(root)
    root.mainloop()
