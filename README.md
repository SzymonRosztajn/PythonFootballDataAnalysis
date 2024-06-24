# Football Data Analysis

## Opis projektu

Niniejszy projekt ma na celu analizę danych piłkarzy biorących udział w Euro 2024. Program umożliwia użytkownikowi wczytanie i eksplorację zbioru danych, dokonywanie prostych manipulacji oraz generowanie wykresów na podstawie wybranych danych. Projekt został stworzony z wykorzystaniem bibliotek NumPy, Pandas, Matplotlib i Seaborn.

## Funkcjonalności

1. **Wczytywanie i eksploracja danych**
   - Umożliwia użytkownikowi wczytanie zbioru danych z pliku CSV.
   - Wyświetlanie kolumn w zbiorze danych.

2. **Analiza danych**
   - Wyświetlanie podstawowych statystyk.
   - Generowanie wniosków z analizy danych.

3. **Manipulacja danych**
   - Filtrowanie danych według wartości lub zakresu.
   - Konwersja kolumn kategorycznych na wartości numeryczne.
   - Sortowanie danych według wybranej kolumny.

4. **Wizualizacja danych**
   - Tworzenie histogramów, wykresów słupkowych i wykresów rozrzutu.

## Struktura projektu

Projekt jest zorganizowany w następujący sposób:

- **data/**: Katalog zawierający plik CSV z danymi piłkarzy.
- **src/**: Katalog zawierający pliki źródłowe projektu.
  - `data_loader.py`: Klasa do wczytywania danych z pliku CSV.
  - `data_analyzer.py`: Klasa do analizy danych, zawierająca metody do filtrowania, sortowania, generowania statystyk i wniosków.
  - `data_visualizer.py`: Klasa do wizualizacji danych, zawierająca metody do tworzenia różnych typów wykresów.
  - `utils.py`: Funkcje pomocnicze, takie jak konwersja kolumn kategorycznych na numeryczne.
  - `main.py`: Główna klasa programu, obsługująca interakcję z użytkownikiem i wywołująca odpowiednie metody z pozostałych klas.
- **tests/**: Katalog zawierający testy jednostkowe.
  - `test_data_analyzer.py`: Testy jednostkowe dla klasy `DataAnalyzer`.
  - `test_data_visualizer.py`: Testy jednostkowe dla klasy `DataVisualizer`.

## Metody i techniki analizy danych

Program wykorzystuje następujące metody i techniki analizy danych:

1. Metoda `basic_statistics` klasy `DataAnalyzer` korzysta z funkcji `describe` z biblioteki Pandas, aby wygenerować podstawowe statystyki dla danych numerycznych, takie jak `count`, `mean`, `std`, `min`, `25%`, `50%`, `75%`, `max`.

2. Metoda `filter_data` klasy `DataAnalyzer` umożliwia filtrowanie danych według jednej wartości lub zakresu wartości. Filtracja jest dostosowana do typu danych kolumny (numeryczne lub tekstowe).

3.  Metoda `sort_data` klasy `DataAnalyzer` umożliwia sortowanie danych według wybranej kolumny w kolejności rosnącej lub malejącej.

4.  Metoda `convert_column` klasy `DataAnalyzer` konwertuje kolumny kategoryczne na wartości numeryczne przy użyciu funkcji `convert_to_numeric` z pliku `utils.py`.

## Struktura i wzorce projektowe

Projekt jest zorganizowany zgodnie z paradygmatami programowania obiektowego i korzysta z kilku wzorców projektowych:

1. Każda funkcjonalność jest zamknięta w osobnej klasie (`DataLoader`, `DataAnalyzer`, `DataVisualizer`), co zapewnia lepszą organizację kodu i ułatwia jego zarządzanie.

2. Każda klasa jest odpowiedzialna za konkretny aspekt programu: wczytywanie danych (`DataLoader`), analiza danych (`DataAnalyzer`), wizualizacja danych (`DataVisualizer`).

3. Klasa `Main` wstrzykuje obiekty `DataAnalyzer` i `DataVisualizer`, co umożliwia łatwe testowanie i modyfikowanie poszczególnych komponentów programu.

## Uruchamianie testów jednostkowych

Aby uruchomić testy jednostkowe, użyj następującej komendy w katalogu głównym projektu:


python -m unittest discover -s tests:
1. Spowoduje, że unittest przeszuka katalog tests i jego podkatalogi.  
2. Znajdzie pliki testowe, które pasują do wzorca test_*.py. 
3. Zaimportuje znalezione pliki testowe.
4. Wykona wszystkie klasy i metody testowe z tych plików.

Uruchomienie komendy:
```bash
python -m unittest discover -s tests
