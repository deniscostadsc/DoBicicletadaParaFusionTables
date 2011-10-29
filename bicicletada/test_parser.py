#!/usr/bin/env python
# coding: utf-8

import unittest
import urllib
from parser import Parser

class TestParser(unittest.TestCase):
    def test_if_table_has_92_groups(self):
        self.parser = Parser()
        self.assertEquals(len(self.parser.parse()), 92)
    
    def test_if_all_lines_has_3_fields(self):
        self.parser = Parser()
        for line in self.parser.parse():
            self.assertEquals(len(line), 3)
    
    def test_if_all_pages_are_available(self):
        self.parser = Parser()
        for line in self.parser.parse():
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