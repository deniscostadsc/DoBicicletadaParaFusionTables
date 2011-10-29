#coding: utf-8

from page import Page
from parser import Parser

class CSV(object):
    
    def __init__(self):
        self.column_names = ['"Estado"', '"Localização"', '"URL"']
        t = Parser()
        self.csv_table = t.parse()
        self.csv_table.insert(0, self.column_names)
    
    def save_csv(self, filename):
        csv_file = open(filename, 'w')
        for line in self.csv_table:
            csv_file.write(','.join(line))
            csv_file.write('\n')
        csv_file.close()