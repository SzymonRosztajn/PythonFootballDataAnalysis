import seaborn as sns
import matplotlib.pyplot as plt


class DataVisualizer:
    def __init__(self, data, conversion_dicts):
        self.data = data
        self.conversion_dicts = conversion_dicts

    def update_conversion_dicts(self, conversion_dicts):
        self.conversion_dicts = conversion_dicts

    def plot_histogram(self, column):
        if column in self.conversion_dicts:
            labels = self.data[column].apply(lambda x: self.conversion_dicts[column].get(x, x))
            sns.histplot(labels, bins=20, kde=True)
            plt.xlabel(column)
        else:
            sns.histplot(self.data[column], bins=20, kde=True)
            plt.xlabel(column)
        plt.title(f'Histogram of {column}')
        plt.ylabel('Częstotliwość')
        plt.show()

    def plot_bar_chart(self, column):
        if column in self.conversion_dicts:
            labels = self.data[column].apply(lambda x: self.conversion_dicts[column].get(x, x))
            sns.countplot(y=labels, order=labels.value_counts().index)
        else:
            sns.countplot(y=column, data=self.data, order=self.data[column].value_counts().index)
        plt.title(f'Bar Chart of {column}')
        plt.xlabel('Liczba')
        plt.ylabel(column)
        plt.show()

    def plot_scatter(self, column1, column2):
        if self.data[column1].dtype in ['int64', 'float64'] and self.data[column2].dtype in ['int64', 'float64']:
            sns.scatterplot(x=column1, y=column2, data=self.data)
            plt.title(f'Scatter Plot of {column1} vs {column2}')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.show()
        else:
            print("Both columns need to be numeric for scatter plot.")
