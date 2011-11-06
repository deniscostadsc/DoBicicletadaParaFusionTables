#!/usr/bin/env python
# coding: utf-8

import urllib
import unittest
from os.path import isfile
from os import remove
from csv import CSV

class TestCSV(unittest.TestCase):

    def setUp(self):
        self.csv = CSV()

    def test_should_all_lines_have_same_quantity_fields(self):
        field_number = len(self.csv.csv_table[0])
        for line in self.csv.csv_table[1:]:
            self.assertEquals(len(line), field_number)

    def test_first_line_should_have_column_names(self):
        self.assertEquals(', '.join(self.csv.column_names), '"Estado", "Localização", "URL"')

    def test_first_field_should_be_state(self):
        states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas',
                  'Bahia', 'Ceará', 'Distrito Federal',
                  'Espírito Santo', 'Goiás', 'Maranhão',
                  'Mato Grosso', 'Mato Grosso do Sul',
                  'Minas Gerais', 'Pará', 'Paraíba', 'Paraná',
                  'Pernambuco', 'Piauí', 'Rio de Janeiro',
                  'Rio Grande do Norte', 'Rio Grande do Sul',
                  'Rondônia', 'Roraima', 'Santa Catarina',
                  'São Paulo', 'Sergipe', 'Tocantins']
        for line in self.csv.csv_table[1:]:
            self.assertIn(line[0][1:-1], states)

    def test_last_field_should_be_url_http(self):
        for line in self.csv.csv_table[1:]:
            self.assertRegexpMatches(line[2], r'^"http://www.bicicletada.org/')

    def test_should_save_csv_as_file(self):
        self.csv.save_csv('XXXXXXXXXXXXXXXXX_my_csv_test_file.csv')
        self.assertTrue(isfile('XXXXXXXXXXXXXXXXX_my_csv_test_file.csv'))
        remove('XXXXXXXXXXXXXXXXX_my_csv_test_file.csv')
    
if __name__ == '__main__':
    unittest.main()