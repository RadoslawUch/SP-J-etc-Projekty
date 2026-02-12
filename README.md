# 1. System Automatyzacji Biurowej FastAPI (Client-Server)

Kompleksowy system narzędziowy zbudowany w Pythonie, który łączy lokalną aplikację GUI z serwerem raportującym. Projekt demonstruje integrację technologii backendowych i frontendowych w celu automatyzacji powtarzalnych zadań biurowych.

##  Funkcjonalności

- Masowy Generator PDF: Automatyczne tworzenie kart mieszkań na podstawie danych z pliku Excel (.xlsx). Obsługuje polskie znaki i generuje osobne pliki dla każdego wiersza.
- Inteligentny Sprzątacz: Automatyczne sortowanie plików w wybranym folderze do kategorii (Dokumenty, Obrazy, Inne).
- System Raportowania API: Aplikacja po każdym wykonanym zadaniu wysyła raport do serwera zewnętrznego przez protokół HTTP.

##  Technologie

- Język: Python 3.x
- GUI: Tkinter
- Backend/API: FastAPI + Uvicorn
- Biblioteki: Pandas, FPDF, Requests

##  Struktura Projektu

- `serwer.py` - Backend API (odbiorca raportów).
- `portfolio.py` - Frontend App (nadawca raportów i logika biznesowa).

##  Jak uruchomić:
- Wymagany Python 3.x.
- KROK 1: Uruchom plik `serwer.py`.
- KROK 2: Uruchom plik `portfolio.py`.



# 2. System Pracowniczy (`RegLog.py`)

Prosta aplikacja GUI zbudowana w Pythonie, służąca do rejestracji czasu pracy.

## Funkcjonalności
- Logowanie i rejestracja (dane zapisywane w JSON)
- Stoper mierzący czas pracy
- Interaktywny interfejs (zmiana kolorów przycisków)

## Jak uruchomić
- Wymagany Python 3.x.
- Uruchom plik główny:
 `RegLog.py`



# 3. Saper Pro ( `Saper.py`)

Projekt klasycznej gry logicznej Saper, zaimplementowany w języku Python z wykorzystaniem biblioteki Tkinter. 
Wersja ta zawiera zaawansowane mechanizmy poprawiające płynność rozgrywki i eliminujące błędy losowe.

## Kluczowe Funkcje

* **Logika Bezpiecznego Startu**: Gra generuje rozmieszczenie min dopiero po pierwszym kliknięciu użytkownika. System gwarantuje, że pole startowe oraz jego bezpośrednie sąsiedztwo (obszar 3x3) są wolne od min, co zawsze skutkuje otwarciem obszaru na początku gry.
* **Mechanizm Chordingu**: Funkcja pozwalająca na szybkie odkrywanie pól sąsiadujących z cyfrą, jeśli wokół niej postawiono już odpowiednią liczbę flag.
* **Automatyczne Odkrywanie (Auto-fill)**: Implementacja algorytmu rekurencyjnego, który natychmiastowo odkrywa puste obszary planszy aż do napotkania pól sąsiadujących z minami.
* **Wbudowany Stoper i Licznik Min**: Monitorowanie czasu gry w sekundach oraz dynamiczne odliczanie pozostałych min na podstawie postawionych flag.

## Obsługa i Sterowanie

| Akcja | Sterowanie |
| :--- | :--- |
| Odkrycie pola | Lewy Przycisk Myszy (LPM) |
| Postawienie flagi | Prawy Przycisk Myszy (PPM) |
| Wykonanie Chordingu | Podwójny LPM lub Kółko Myszy |
| Resetowanie gry | Przycisk resetu (środkowy panel górny) |

## Poziomy Trudności

Gra oferuje trzy predefiniowane tryby dostępne w menu górnym:

1.  **Łatwy**: Plansza 9x9, 10 min.
2.  **Normalny**: Plansza 12x20, 35 min.
3.  **Trudny**: Plansza 16x30, 100 min.

## Wymagania Techniczne

* **Środowisko**: Python 3.x
* **Biblioteki**: Tkinter (standardowy moduł Pythona)
* **System operacyjny**: Dowolny system obsługujący środowisko Python


## Jak uruchomić
- Wymagany Python 3.x.
- Uruchom plik główny:
 `Saper.py`


## Podgląd Interfejsu

* **🙂**: Nowa gra / Reset.
* **😵**: Koniec gry (trafienie na minę).
* **😎**: Wygrana!





# 4. Kalkulator Matematyczny (`Kalkulator.py`)

Uproszczony kalkulator konsolowy stworzony w Pythonie. 
Program pozwala na błyskawiczne obliczanie dowolnej liczby działań matematycznych bez konieczności deklarowania ich ilości na starcie.

## Funkcjonalności

* **Nielimitowane obliczenia**: Program działa w ciągłej pętli, pozwalając na wpisywanie kolejnych zadań bez przerwy.
* **Odporność na błędy**: Dzięki zastosowaniu bloku `try-except`, błędnie wpisane działanie (np. niedokończone równanie) nie zawiesza programu.
* **Bezpośrednie przetwarzanie**: Wykorzystuje funkcję `eval()` do natychmiastowej interpretacji tekstu jako operacji matematycznej.
* **Czysty interfejs**: Brak zbędnych pytań o liczbę zestawów – wpisujesz i od razu widzisz wynik.

## Jak to działa

W przeciwieństwie do poprzednich wersji, ten program nie wymaga podawania liczby zadań na początku:
1. Uruchom skrypt.
2. Wpisz dowolne działanie (np. `2+2*2`) i naciśnij Enter.
3. Program wyświetli wynik i od razu będzie gotowy na kolejne zadanie.



## Technologie

* **Python 3.x**: Główny język programowania.
* **sys.stdin**: Służy do ciągłego odczytywania strumienia danych od użytkownika.
* **Error Handling**: Mechanizm zapobiegający wyłączaniu się programu przy błędach składniowych.

## Jak uruchomić

- Wymagany Python 3.x.
- Uruchom plik główny:
`Kalkulator.py`

## Przykład Działania

5+5
10
12*3
36
100/2
50
