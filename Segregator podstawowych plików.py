import os
import shutil

FOLDER_DO_SPRZATANIA = os.path.dirname(os.path.abspath(__file__))

MAPA_FOLDEROW = {
    "Obrazy": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
    "Dokumenty_PDF": [".pdf"],
    "Arkusze_Excel": [".xlsx", ".xls", ".csv"],
    "Aplikacje": [".exe", ".msi"],
    "Skroty_aplikacji": [".url", ".lnk"],
    "Dokumenty_Tekstowe": [".docx", ".doc", ".txt"]
}

def segreguj_pliki():
    for nazwa_pliku in os.listdir(FOLDER_DO_SPRZATANIA):
        sciezka_pliku = os.path.join(FOLDER_DO_SPRZATANIA, nazwa_pliku)
        
        if os.path.isdir(sciezka_pliku) or nazwa_pliku == os.path.basename(__file__):
            continue
            
        rozszerzenie = os.path.splitext(nazwa_pliku)[1].lower()
        
        for folder, rozszerzenia in MAPA_FOLDEROW.items():
            if rozszerzenie in rozszerzenia:
                cel_folder = os.path.join(FOLDER_DO_SPRZATANIA, folder)
                
                if not os.path.exists(cel_folder):
                    os.makedirs(cel_folder)
                
                try:
                    shutil.move(sciezka_pliku, os.path.join(cel_folder, nazwa_pliku))
                    print(f"Przeniesiono: {nazwa_pliku} -> {folder}")
                except Exception as e:
                    print(f"Blad: {e}")
                break

if __name__ == "__main__":
    segreguj_pliki()
    print("Zakonczono.")
    input("Enter aby zamknac...")
