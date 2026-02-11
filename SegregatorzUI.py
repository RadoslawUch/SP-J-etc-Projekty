import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil

class PortfolioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Python Portfolio - System Automatyzacji")
        self.root.geometry("900x550")
        
        # Kolory Dashboardu
        self.menu_color = "#2c3e50"
        self.bg_color = "#ecf0f1"
        
        # Główny podział
        self.sidebar = tk.Frame(self.root, bg=self.menu_color, width=220)
        self.sidebar.pack(side="left", fill="y")
        
        self.main_content = tk.Frame(self.root, bg=self.bg_color)
        self.main_content.pack(side="right", expand=True, fill="both")

        self.stworz_przyciski()
        self.pokaz_narzedzia()

    def stworz_przyciski(self):
        btn_style = {
            "bg": self.menu_color, 
            "fg": "white", 
            "relief": "flat", 
            "pady": 20, 
            "font": ("Arial", 11, "bold"),
            "activebackground": "#34495e",
            "activeforeground": "#3498db",
            "cursor": "hand2"
        }
        
        tk.Button(self.sidebar, text="👤 O MNIE", **btn_style, command=self.pokaz_home).pack(fill="x")
        tk.Button(self.sidebar, text="🧹 SPRZĄTACZ", **btn_style, command=self.pokaz_narzedzia).pack(fill="x")

    def wyczysc_ekran(self):
        for widget in self.main_content.winfo_children():
            widget.destroy()

    def pokaz_home(self):
        self.wyczysc_ekran()
        tk.Label(self.main_content, text="Witaj w moim Portfolio", font=("Arial", 26, "bold"), bg=self.bg_color, fg="#2c3e50").pack(pady=40)
        
        tekst_powitalny = (
            "Prezentuję aplikację typu 'File Organizer'.\n\n"
            "Projekt demonstruje praktyczne zastosowanie języka Python w:\n"
            "• Zarządzaniu strukturą plików i folderów\n"
            "• Tworzeniu nowoczesnych interfejsów graficznych (GUI)\n"
            "• Automatyzacji powtarzalnych zadań biurowych"
        )
        
        tk.Label(self.main_content, text=tekst_powitalny, font=("Arial", 12), bg=self.bg_color, justify="center", pady=20).pack()

    def pokaz_narzedzia(self):
        self.wyczysc_ekran()
        tk.Label(self.main_content, text="Inteligentny Porządkownik Plików", font=("Arial", 20, "bold"), bg=self.bg_color, fg="#2980b9").pack(pady=20)
        
        # Kontener centralny
        ramka = tk.Frame(self.main_content, bg="white", padx=40, pady=40, highlightbackground="#bdc3c7", highlightthickness=1)
        ramka.pack(pady=20, padx=50, fill="x")
        
        instrukcja = (
            "Instrukcja:\n"
            "1. Kliknij przycisk poniżej\n"
            "2. Wybierz folder, w którym panuje bałagan\n"
            "3. Program automatycznie posegreguje pliki do kategorii"
        )
        
        tk.Label(ramka, text=instrukcja, bg="white", font=("Arial", 11), justify="left").pack(pady=(0, 30))
        
        tk.Button(ramka, text="📁 WYBIERZ FOLDER I URUCHOM", command=self.posprzataj_folder, 
                  bg="#2ecc71", fg="white", font=("Arial", 12, "bold"), padx=20, pady=12, relief="raised", cursor="hand2").pack()

    def posprzataj_folder(self):
        sciezka = filedialog.askdirectory()
        if not sciezka: return

        rozszerzenia = {
            'Obrazy': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.webp'],
            'Dokumenty': ['.pdf', '.docx', '.txt', '.xlsx', '.csv', '.pptx', '.doc', '.odt'],
            'Archiwa': ['.zip', '.rar', '.7z', '.tar'],
            'Filmy': ['.mp4', '.mkv', '.avi', '.mov'],
            'Muzyka': ['.mp3', '.wav', '.flac', '.m4a'],
            'Instalki': ['.exe', '.msi', '.apk', '.bat'],
            'Programowanie': ['.py', '.html', '.css', '.js', '.json', '.cpp', '.sql']
        }

        try:
            licznik = 0
            path_inne = os.path.join(sciezka, 'Inne')
            
            for plik in os.listdir(sciezka):
                full_path = os.path.join(sciezka, plik)
                
                if os.path.isfile(full_path):
                    ext = os.path.splitext(plik)[1].lower()
                    znaleziono = False
                    
                    for kategoria, exts in rozszerzenia.items():
                        if ext in exts:
                            target_dir = os.path.join(sciezka, kategoria)
                            os.makedirs(target_dir, exist_ok=True)
                            shutil.move(full_path, os.path.join(target_dir, plik))
                            znaleziono = True
                            licznik += 1
                            break
                    
                    if not znaleziono:
                        os.makedirs(path_inne, exist_ok=True)
                        shutil.move(full_path, os.path.join(path_inne, plik))
                        licznik += 1
            
            messagebox.showinfo("Zakończono", f"Sukces! Uporządkowano {licznik} plików.")
            
        except Exception as e:
            messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany problem: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = PortfolioApp(root)
    root.mainloop()
