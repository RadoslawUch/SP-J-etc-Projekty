import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
import pandas as pd
from fpdf import FPDF
import requests

class PortfolioKombajn:
    def __init__(self, root):
        self.root = root
        self.root.title("System Automatyzacji - Portfolio")
        self.root.geometry("950x600")
        
        self.menu_color = "#2c3e50"
        self.bg_color = "#ecf0f1"
        
        self.sidebar = tk.Frame(self.root, bg=self.menu_color, width=220)
        self.sidebar.pack(side="left", fill="y")
        
        self.main_content = tk.Frame(self.root, bg=self.bg_color)
        self.main_content.pack(side="right", expand=True, fill="both")

        self.stworz_menu()
        self.pokaz_home()

    def stworz_menu(self):
        btn_style = {
            "bg": self.menu_color, "fg": "white", "relief": "flat", "pady": 20, 
            "font": ("Arial", 11, "bold"), "activebackground": "#34495e", "cursor": "hand2"
        }
        tk.Button(self.sidebar, text="👤 O MNIE", **btn_style, command=self.pokaz_home).pack(fill="x")
        tk.Button(self.sidebar, text="🧹 SPRZATACZ", **btn_style, command=self.pokaz_sprzatacza).pack(fill="x")
        tk.Button(self.sidebar, text="📄 GENERATOR PDF", **btn_style, command=self.pokaz_generatora).pack(fill="x")

    def wyczysc_ekran(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def powiadom_serwer(self, nazwa_zadania, wynik):
        url = "http://127.0.0.1:8000/odbierz-raport"
        dane = {"wiadomosc": nazwa_zadania, "liczba_plikow": wynik}
        try:
            requests.post(url, json=dane, timeout=1)
        except:
            pass

    def pokaz_home(self):
        self.wyczysc_ekran()
        tk.Label(self.main_content, text="Panel Zarzadzania Automatyzacja", font=("Arial", 24, "bold"), bg=self.bg_color).pack(pady=40)
        tk.Label(self.main_content, text="Wybierz narzedzie z menu po lewej stronie.", font=("Arial", 12), bg=self.bg_color).pack()

    def pokaz_sprzatacza(self):
        self.wyczysc_ekran()
        tk.Label(self.main_content, text="Porzadkownik Plikow", font=("Arial", 20, "bold"), bg=self.bg_color).pack(pady=20)
        tk.Button(self.main_content, text="📂 WYBIERZ FOLDER", bg="#2ecc71", fg="white", 
                  font=("Arial", 12, "bold"), padx=20, pady=10, command=self.logika_sprzatacza).pack(pady=50)

    def logika_sprzatacza(self):
        folder = filedialog.askdirectory()
        if not folder: return
        licznik = 0
        kategorie = {'Dokumenty': ['.pdf', '.docx', '.xlsx', '.txt'], 'Obrazy': ['.jpg', '.png', '.jpeg']}
        for plik in os.listdir(folder):
            if os.path.isfile(os.path.join(folder, plik)):
                ext = os.path.splitext(plik)[1].lower()
                cel = "Inne"
                for kat, exts in kategorie.items():
                    if ext in exts: cel = kat
                folder_cel = os.path.join(folder, cel)
                os.makedirs(folder_cel, exist_ok=True)
                shutil.move(os.path.join(folder, plik), os.path.join(folder_cel, plik))
                licznik += 1
        messagebox.showinfo("Sukces", f"Uporzadkowano {licznik} plikow.")
        self.powiadom_serwer("Sprzatanie", licznik)

    def pokaz_generatora(self):
        self.wyczysc_ekran()
        tk.Label(self.main_content, text="Masowy Generator PDF", font=("Arial", 20, "bold"), bg=self.bg_color).pack(pady=20)
        tk.Button(self.main_content, text="📑 WYBIERZ PLIK EXCEL", bg="#e67e22", fg="white", 
                  font=("Arial", 12, "bold"), padx=20, pady=10, command=self.logika_pdf).pack(pady=50)

    def logika_pdf(self):
        sciezka_excel = filedialog.askopenfilename(filetypes=[("Excel", "*.xlsx")])
        if not sciezka_excel: return
        font_win = r"C:\Windows\Fonts\arial.ttf"
        try:
            df = pd.read_excel(sciezka_excel)
            df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
            folder_wyjsciowy = os.path.dirname(sciezka_excel)
            for i, wiersz in df.iterrows():
                pdf = FPDF()
                pdf.add_page()
                if os.path.exists(font_win):
                    pdf.add_font('Standard', '', font_win, uni=True)
                    pdf.set_font('Standard', '', 12)
                else:
                    pdf.set_font('Arial', '', 12)
                
                pdf.cell(0, 10, f"KARTA MIESZKANIA NR {i+1}", ln=1, align='C')
                pdf.ln(10)
                for k, v in wiersz.items():
                    tekst = f"{str(k)}: {str(v)}".encode('latin-1', 'replace').decode('latin-1')
                    pdf.cell(0, 10, tekst, ln=1)
                pdf.output(os.path.join(folder_wyjsciowy, f"Karta_{i+1}.pdf"))
            messagebox.showinfo("Sukces", f"Wygenerowano {len(df)} dokumentow PDF.")
            self.powiadom_serwer("Generowanie PDF", len(df))
        except Exception as e:
            messagebox.showerror("Blad", f"Wystapil problem: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioKombajn(root)
    root.mainloop()
