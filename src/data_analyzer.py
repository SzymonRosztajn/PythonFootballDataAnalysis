import pandas as pd

from src.utils import convert_to_numeric


class DataAnalyzer:
    def __init__(self, data):
        self.data = data
        self.conversion_dicts = {}

    def filter_data(self, column, value=None, min_value=None, max_value=None):
        if value is not None:
            if self.data[column].dtype == 'object':
                filtered_data = self.data[self.data[column] == value]
            else:
                filtered_data = self.data[self.data[column] == float(value)]
        elif min_value is not None and max_value is not None:
            if self.data[column].dtype != 'object':
                filtered_data = self.data[
                    (self.data[column] >= float(min_value)) & (self.data[column] <= float(max_value))]
            else:
                print("Zakres filtrowania nie jest obsługiwany dla kolumn tekstowych.")
                filtered_data = pd.DataFrame()
        else:
            print("Podaj wartość lub zakres do filtrowania.")
            filtered_data = pd.DataFrame()

        if not filtered_data.empty:
            sorted_filtered_data = filtered_data.sort_values(by=column, ascending=True)
        else:
            sorted_filtered_data = filtered_data

        return sorted_filtered_data

    def sort_data(self, column, ascending=True):
        if column in self.data.columns:
            sorted_data = self.data.sort_values(by=column, ascending=ascending)
        else:
            print(f"Kolumna {column} nie istnieje w danych.")
            sorted_data = pd.DataFrame()
        return sorted_data

    def basic_statistics(self):
        numeric_data = self.data.select_dtypes(include=['number'])
        stats = numeric_data.describe().T
        stats_formatted = stats.copy()
        for col in stats.columns:
            stats_formatted[col] = stats[col].map(lambda x: f"{x:,.2f}")
        return stats_formatted

    def column_statistics(self):
        stats = {}
        for column in self.data.columns:
            if self.data[column].dtype in ['int64', 'float64']:
                max_val = self.data[column].max()
                min_val = self.data[column].min()
                mean_val = self.data[column].mean()
                stats[column] = {
                    'Maximum': max_val,
                    'Minimum': min_val,
                    'Mean': mean_val
                }
        return stats

    def generate_insights(self):
        insights = "Wnioski z analizy danych:\n"
        numeric_data = self.data.select_dtypes(include=['number'])
        for column in numeric_data.columns:
            max_val = numeric_data[column].max()
            min_val = numeric_data[column].min()
            mean_val = numeric_data[column].mean()
            insights += (f"Kolumna '{column}':\n"
                         f" - Wartość maksymalna: {max_val}\n"
                         f" - Wartość minimalna: {min_val}\n"
                         f" - Wartość średnia: {mean_val}\n\n")
        return insights

    def convert_column(self, column):
        self.data, conversion_dict = convert_to_numeric(self.data, column)
        self.conversion_dicts[column] = conversion_dict
        return conversion_dict
