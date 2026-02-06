import os
import sys

try:
    import pandas as pd
    from fpdf import FPDF
    from fpdf.enums import XPos, YPos
except ImportError:
    sys.exit()

FOLDER = os.path.dirname(os.path.abspath(__file__))
PLIK_EXCEL = os.path.join(FOLDER, "Dane.xlsx")
FONT_PATH = r"C:\Windows\Fonts\arial.ttf"

def generuj():
    if not os.path.exists(PLIK_EXCEL):
        return

    df = pd.read_excel(PLIK_EXCEL)
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    for i, wiersz in df.iterrows():
        pdf = FPDF()
        pdf.add_page()
        pdf.add_font('PolandArial', '', FONT_PATH)
        pdf.set_font('PolandArial', '', 16)
        
        pdf.cell(0, 10, text=f"KARTA MIESZKANIA NR {i+1}", 
                 new_x=XPos.LMARGIN, new_y=YPos.NEXT, align='C')
        pdf.ln(10)
        
        pdf.set_font('PolandArial', '', 12)
        for kolumna, wartosc in wiersz.items():
            pdf.cell(0, 10, text=f"{kolumna}: {wartosc}", 
                     new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            
        pdf.output(os.path.join(FOLDER, f"Mieszkanie_{i+1}.pdf"))
        print(f"Wygenerowano: Mieszkanie_{i+1}.pdf")

if __name__ == "__main__":
    generuj()
    input("\nGotowe. Enter = Wyjscie")
