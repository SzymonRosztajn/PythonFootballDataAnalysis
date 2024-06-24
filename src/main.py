import pandas as pd
from data_loader import DataLoader
from data_analyzer import DataAnalyzer
from data_visualizer import DataVisualizer

class Main:
    def __init__(self, file_path):
        self.loader = DataLoader(file_path)
        self.data = self.loader.load_data()
        if self.data is not None:
            self.analyzer = DataAnalyzer(self.data)
            self.visualizer = DataVisualizer(self.data, self.analyzer.conversion_dicts)
            # Ustawienia Pandas
            pd.set_option('display.max_columns', None)
            pd.set_option('display.max_rows', None)
            pd.set_option('display.width', 1000)
            pd.set_option('display.colheader_justify', 'center')
            pd.set_option('display.precision', 2)

    def display_menu(self):
        print("\nMenu:")
        print("1. Wyświetl kolumny w zbiorze danych")
        print("2. Wyświetl podstawowe statystyki")
        print("3. Histogram kolumny")
        print("4. Wykres słupkowy kolumny")
        print("5. Wykres rozrzutu dwóch kolumn")
        print("6. Filtrowanie danych")
        print("7. Konwersja typu danych")
        print("8. Generuj wnioski z analizy danych")
        print("9. Wyświetl słownik konwersji")
        print("10. Sortowanie danych")
        print("0. Wyjście")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Wybierz opcję: ")

            if choice == '1':
                print("Kolumny w zbiorze danych:", self.data.columns)
            elif choice == '2':
                stats = self.analyzer.basic_statistics()
                print("Podstawowe statystyki:\n", stats)
            elif choice == '3':
                column = input("Podaj nazwę kolumny: ")
                self.visualizer.plot_histogram(column)
            elif choice == '4':
                column = input("Podaj nazwę kolumny: ")
                self.visualizer.plot_bar_chart(column)
            elif choice == '5':
                column1 = input("Podaj nazwę kolumny dla osi X: ")
                column2 = input("Podaj nazwę kolumny dla osi Y: ")
                self.visualizer.plot_scatter(column1, column2)
            elif choice == '6':
                column = input("Podaj nazwę kolumny do filtrowania: ")
                filter_type = input("Czy chcesz filtrować według jednej wartości (wpisz 'wartość') czy zakresu (wpisz 'zakres')? ")
                if filter_type == 'wartość':
                    value = input(f"Podaj wartość do filtrowania dla kolumny {column}: ")
                    filtered_data = self.analyzer.filter_data(column, value=value)
                elif filter_type == 'zakres':
                    min_value = input(f"Podaj minimalną wartość do filtrowania dla kolumny {column}: ")
                    max_value = input(f"Podaj maksymalną wartość do filtrowania dla kolumny {column}: ")
                    filtered_data = self.analyzer.filter_data(column, min_value=min_value, max_value=max_value)
                else:
                    print("Niepoprawny wybór. Spróbuj ponownie.")
                    continue
                print(f"Przefiltrowane i posortowane dane po kolumnie {column}:\n", filtered_data)
            elif choice == '7':
                column = input("Podaj nazwę kolumny do konwersji: ")
                conversion_dict = self.analyzer.convert_column(column)
                self.visualizer.update_conversion_dicts(self.analyzer.conversion_dicts)
                print(f"Kolumna {column} skonwertowana do wartości numerycznych.")
                print("Słownik konwersji:", conversion_dict)
            elif choice == '8':
                print(self.analyzer.generate_insights())
            elif choice == '9':
                if self.analyzer.conversion_dicts:
                    for column, conversion_dict in self.analyzer.conversion_dicts.items():
                        print(f"\nKolumna: {column}")
                        for key, value in conversion_dict.items():
                            print(f"{key}: {value}")
                else:
                    print("Brak słowników konwersji.")
            elif choice == '10':
                column = input("Podaj nazwę kolumny do sortowania: ")
                order = input("Sortować rosnąco? (tak/nie): ").strip().lower()
                ascending = True if order == 'tak' else False
                sorted_data = self.analyzer.sort_data(column, ascending=ascending)
                print(f"Dane posortowane po kolumnie {column}:\n", sorted_data)
            elif choice == '0':
                print("Wyjście z programu.")
                break
            else:
                print("Niepoprawny wybór, spróbuj ponownie.")

if __name__ == '__main__':
    file_path = 'data/euro2024_players.csv'
    main = Main(file_path)
    main.run()
