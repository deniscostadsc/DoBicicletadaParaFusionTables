#!/usr/bin/env python
# coding: utf-8

import unittest
from parser import Parser

class TestParser(unittest.TestCase):
    
    def test_if_all_lines_has_3_fields(self):
        parser = Parser()
        for line in parser.parse():
            self.assertEquals(len(line), 3)
    
if __name__ == '__main__':
    unittest.main()
