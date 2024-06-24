import unittest
import pandas as pd

from src.data_analyzer import DataAnalyzer


class TestDataAnalyzer(unittest.TestCase):

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
        self.analyzer = DataAnalyzer(self.df)

    def test_basic_statistics(self):
        stats = self.analyzer.basic_statistics()
        self.assertEqual(stats.loc['Wiek', 'mean'], '26.67')
        self.assertEqual(stats.loc['Wzrost', 'mean'], '181.67')
        self.assertEqual(stats.loc['Wsytępy', 'mean'], '100.00')
        self.assertEqual(stats.loc['Gole', 'mean'], '11.67')
        self.assertEqual(stats.loc['WartośćRynkowa', 'mean'], '1,500,000.00')

    def test_filter_data_by_value(self):
        filtered_data = self.analyzer.filter_data('Klub', value='ClubA')
        self.assertEqual(len(filtered_data), 2)
        self.assertTrue((filtered_data['Klub'] == 'ClubA').all())

    def test_filter_data_by_range(self):
        filtered_data = self.analyzer.filter_data('Wiek', min_value=25, max_value=35)
        self.assertEqual(len(filtered_data), 2)
        self.assertTrue((filtered_data['Wiek'] >= 25).all() and (filtered_data['Wiek'] <= 35).all())

    def test_sort_data(self):
        sorted_data = self.analyzer.sort_data('Wiek', ascending=True)
        self.assertEqual(sorted_data.iloc[0]['Wiek'], 22)
        self.assertEqual(sorted_data.iloc[-1]['Wiek'], 30)


if __name__ == '__main__':
    unittest.main()
