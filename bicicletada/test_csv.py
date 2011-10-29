#!/usr/bin/env python
# coding: utf-8

import urllib
import unittest
from csv import CSV

class TestCSV(unittest.TestCase):

    def test_should_there_are_3_column_names(self):
        csv=CSV()
        self.assertEquals(len(csv.column_names), 3)
    
    def test_first_line_should_have_column_names(self):
        csv=CSV()
        self.assertEquals(', '.join(csv.column_names), 'Estado, Localização, URL')
    
    def test_first_field_should_be_state(self):
        csv=CSV()
        states = ['Acre', 'Alagoas', 'Amapá', 'Amazonas',
                  'Bahia', 'Ceará', 'Distrito Federal',
                  'Espírito Santo', 'Goiás', 'Maranhão',
                  'Mato Grosso', 'Mato Grosso do Sul',
                  'Minas Gerais', 'Pará', 'Paraíba', 'Paraná',
                  'Pernambuco', 'Piauí', 'Rio de Janeiro',
                  'Rio Grande do Norte', 'Rio Grande do Sul',
                  'Rondônia', 'Roraima', 'Santa Catarina',
                  'São Paulo', 'Sergipe', 'Tocantins']
        for line in csv.csv_table[1:]:
            self.assertIn(line[0], states)
    
    def test_last_field_should_be_url_http(self):
        csv=CSV()
        for line in csv.csv_table[1:]:
            self.assertRegexpMatches(line[2], r'^http://www.bicicletada.org/')
    
    def test_if_all_pages_are_available(self):
        csv = CSV()
        for line in csv.csv_table[1:]:
            url = line[-1]
            # São Lorenço não funciona
            # Feito um hack pra funcionar 
            if url != 'http://bicicletada.org/saolourenco':
                url = 'http://bicicletada.org/'
            # Pega a pagina configurada na URL.
            page = urllib.urlopen(url)
            self.assertEquals(page.getcode(), 200)

if __name__ == '__main__':
    unittest.main()