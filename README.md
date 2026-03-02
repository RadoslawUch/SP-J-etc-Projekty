

# Kalkulator Matematyczny (`Kalkulator.py`)

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
