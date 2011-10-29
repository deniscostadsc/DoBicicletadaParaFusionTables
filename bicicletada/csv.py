#coding: utf-8

from page import Page
from parser import Parser

class CSV(object):
    def __init__(self):
        self.column_names = ['Estado', 'Localização', 'URL']
        t = Parser()
        self.csv_table = t.parse()
        self.csv_table.insert(0, self.column_names)
