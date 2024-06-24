import unittest
import pandas as pd

from src.data_visualizer import DataVisualizer


class TestDataVisualizer(unittest.TestCase):

    def setUp(self):
        data = {
            'Imie': ['Player1', 'Player2', 'Player3'],
            'Pozycja': ['Goalkeeper', 'Midfield', 'Centre-Back'],
            'Wiek': [22, 30, 28],
            'Klub': ['ClubA', 'ClubB', 'ClubA'],
            'Wzrost': [180, 175, 190],
            'LepszaStopa': ['Right', 'Left', 'Right'],
            'Wsytępy': [50, 100, 150],
            'Gole': [10, 20, 5],
            'WartośćRynkowa': [1000000, 2000000, 1500000],
            'Kraj': ['CountryA', 'CountryB', 'CountryA']
        }
        self.df = pd.DataFrame(data)
        conversion_dicts = {
            'Pozycja': {'Goalkeeper': 0, 'Midfiled': 1, 'Centre-Back': 2}
        }
        self.visualizer = DataVisualizer(self.df, conversion_dicts)

    def test_plot_histogram(self):
        try:
            self.visualizer.plot_histogram('Wiek')
        except Exception as e:
            self.fail(f"plot_histogram raised Exception unexpectedly: {e}")

    def test_plot_bar_chart(self):
        try:
            self.visualizer.plot_bar_chart('Pozycja')
        except Exception as e:
            self.fail(f"plot_bar_chart raised Exception unexpectedly: {e}")

    def test_plot_scatter(self):
        try:
            self.visualizer.plot_scatter('Wiek', 'WartośćRynkowa')
        except Exception as e:
            self.fail(f"plot_scatter raised Exception unexpectedly: {e}")

if __name__ == '__main__':
    unittest.main()
