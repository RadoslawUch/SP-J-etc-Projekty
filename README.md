# System Pracowniczy

Prosta aplikacja GUI zbudowana w Pythonie, służąca do rejestracji czasu pracy.

## Funkcjonalności
- Logowanie i rejestracja (dane zapisywane w JSON)
- Stoper mierzący czas pracy
- Interaktywny interfejs (zmiana kolorów przycisków)

## Jak uruchomić
- Wymagany Python 3.x.
- Uruchom plik główny:
 `RegLog.py`




#  Klasyczny Saper

W pełni funkcjonalna, graficzna wersja gry Saper zbudowana w języku Python przy użyciu biblioteki **Tkinter**. Projekt odwzorowuje klasyczną mechanikę znaną z systemów Windows, oferując intuicyjny interfejs i trzy poziomy trudności.


##  Funkcjonalności

* **Interaktywny interfejs**: Klasyczny wygląd z licznikiem pozostałych min oraz cyfrowym stoperem.
* **Mechanika gry**:
    * **Lewy przycisk myszy**: Odkrywanie pól.
    * **Prawy przycisk myszy**: Oznaczanie min flagami 🚩.
    * **Automatyczne odkrywanie**: Funkcja "flood fill" automatycznie otwiera puste obszary bez min.
* **System poziomów**: Możliwość zmiany trudności w trakcie gry poprzez menu górne.
* **Zabezpieczenia**: Program uniemożliwia przypadkowe kliknięcie odkrytego pola lub pola z flagą.


##  Poziomy Trudności

Gra oferuje trzy predefiniowane poziomy, które zmieniają wyzwanie:

| Poziom | Siatka (Wiersze x Kolumny) | Liczba Min |
| :--- | :--- | :--- |
| **Łatwy** | 9 x 9 | 10 |
| **Normalny** | 12 x 20 | 35 |
| **Trudny** | 16 x 30 | 100 |


##  Technologie

Projekt został stworzony z wykorzystaniem standardowych bibliotek Pythona:
* **Tkinter**: Odpowiada za warstwę wizualną i obsługę zdarzeń (okna, przyciski).
* **Random**: Wykorzystywany do losowego rozmieszczania min na planszy.
* **Time**: Obsługuje precyzyjne odmierzanie czasu gry.


## Jak uruchomić
- Wymagany Python 3.x.
- Uruchom plik główny:
 `Saper.py`


## Podgląd Interfejsu

* **🙂**: Nowa gra / Reset.
* **😵**: Koniec gry (trafienie na minę).
* **😎**: Wygrana!