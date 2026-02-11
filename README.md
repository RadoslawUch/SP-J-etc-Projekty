# 1. System Pracowniczy (`RegLog.py`)

Prosta aplikacja GUI zbudowana w Pythonie, służąca do rejestracji czasu pracy.

## Funkcjonalności
- Logowanie i rejestracja (dane zapisywane w JSON)
- Stoper mierzący czas pracy
- Interaktywny interfejs (zmiana kolorów przycisków)

## Jak uruchomić
- Wymagany Python 3.x.
- Uruchom plik główny:
 `RegLog.py`




# 2. Saper Pro - Dokumentacja Projektu ( `Saper.py`)

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






# 3. Generator Kart Mieszkań ( `GeneratorPDF.py`)

Prosta aplikacja do automatycznego generowania dokumentów PDF na podstawie danych zawartych w arkuszu Excel. Skrypt idealnie nadaje się do szybkiego tworzenia ustandaryzowanych kart informacyjnych dla wielu obiektów jednocześnie.


## Funkcjonalności

* **Import danych z Excela**: Automatyczne wczytywanie informacji z pliku `Dane.xlsx`.
* **Generowanie PDF**: Tworzenie osobnego pliku PDF dla każdego wiersza w arkuszu.
* **Formatowanie tekstu**: Każdy dokument posiada wyśrodkowany nagłówek oraz listę parametrów mieszkania.
* **Obsługa polskich znaków**: Wykorzystanie systemowej czcionki Arial do poprawnego wyświetlania treści.
* **Oczyszczanie danych**: Automatyczne usuwanie pustych kolumn ("Unnamed") z arkusza podczas przetwarzania.


## Jak to działa

1. Program szuka pliku o nazwie `Dane.xlsx` w swoim folderze.
2. Odczytuje każdą kolumnę (np. Powierzchnia, Piętro, Liczba pokoi).
3. Tworzy pliki o nazwach `Mieszkanie_1.pdf`, `Mieszkanie_2.pdf` itd.


## Technologie

Projekt wykorzystuje potężne biblioteki do obsługi danych i plików:
* **Pandas**: Służy do odczytu i strukturyzowania danych z arkuszy kalkulacyjnych.
* **fpdf2**: Biblioteka umożliwiająca generowanie dokumentów PDF w Pythonie.
* **OS**: Zarządzanie ścieżkami plików i lokalizacją folderu roboczego.


## Jak uruchomić

- Wymagany Python 3.x.
- Zainstaluj biblioteki: `pip install pandas fpdf2 openpyxl`.
- Upewnij się, że plik `Dane.xlsx` znajduje się w tym samym folderze.
- Uruchom plik główny:
`GeneratorPDF.py`


## Podgląd Wyjścia

* **KARTA MIESZKANIA NR X**: Nagłówek dokumentu.
* **Dane**: Wszystkie pary Kolumna: Wartość przeniesione prosto z Excela.



# 4. Auto-Segregator Plików (`Segregator podstawowych plików.py`)

Prosty i skuteczny skrypt w języku Python służący do automatycznego porządkowania bałaganu w wybranym folderze. Program skanuje pliki i rozdziela je do odpowiednich podfolderów na podstawie ich rozszerzeń.


## Funkcjonalności

* **Automatyczne sortowanie**: Rozpoznaje typy plików i przenosi je do dedykowanych folderów (np. Obrazy, Dokumenty).
* **Bezpieczeństwo**: Skrypt automatycznie ignoruje samego siebie podczas sprzątania, aby zapobiec przeniesieniu kodu źródłowego.
* **Dynamiczne tworzenie folderów**: Jeśli folder docelowy (np. "Arkusze_Excel") nie istnieje, program stworzy go automatycznie.
* **Obsługa błędów**: System raportuje w konsoli każde udane przeniesienie lub ewentualny błąd dostępu do pliku.


## Jak to działa

Program posiada zdefiniowaną mapę rozszerzeń, która przypisuje pliki do konkretnych kategorii:
* **Obrazy**: .jpg, .png, .gif, .svg itp.
* **Dokumenty**: .pdf, .docx, .txt.
* **Arkusze**: .xlsx, .csv.
* **Aplikacje i skróty**: .exe, .msi, .url, .lnk.


## Technologie

Projekt opiera się na standardowych bibliotekach Pythona, co gwarantuje szybkość działania bez instalowania dodatków:
* **OS**: Służy do skanowania zawartości folderów i zarządzania ścieżkami.
* **Shutil**: Wykorzystywany do operacji przenoszenia plików między lokalizacjami.


## Jak uruchomić

- Wymagany Python 3.x.
- Umieść skrypt w folderze, który chcesz posprzątać.
- Uruchom plik główny:
`Segregator podstawowych plików.py`


## Podgląd Działania

* **Przeniesiono: zdjęcie.jpg -> Obrazy**: Komunikat o sukcesie w konsoli.
* **Zakończono**: Informacja o sfinalizowaniu porządków.




# 5. Kalkulator Matematyczny (`Kalkulator.py`)

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

```text
5+5
10
12*3
36
100/2
50