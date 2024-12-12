# tests/test_data_preprocessing.py

import unittest
import pandas as pd
from ldc.data_preprocessing import load_and_clean_data

class TestDataPreprocessing(unittest.TestCase):
    def test_clean_data(self):
        data = pd.DataFrame({
            'ALB': [None, 3.5, 3.2],
            'Sex': ['m', 'f', 'm'],
            'Category': ['0=Blood Donor', '2=Hepatitis', '3=Fibrosis']
        })

        pathToData = './data/HepatitisCdata.csv'

        cleaned_data = load_and_clean_data(pathToData)

        self.assertFalse(cleaned_data.isnull().values.any())

        self.assertTrue('ALB' in cleaned_data.columns)

if __name__ == '__main__':
    unittest.main()
