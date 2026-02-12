import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Raport(BaseModel):
    wiadomosc: str
    liczba_plikow: int

@app.post("/odbierz-raport")
def odbierz_dane(raport: Raport):
    print("\n" + "="*30)
    print(f"!!! NOWY RAPORT !!!")
    print(f"CO ZROBIONO: {raport.wiadomosc}")
    print(f"ILE: {raport.liczba_plikow}")
    print("="*30 + "\n")
    return {"status": "Sukces"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
