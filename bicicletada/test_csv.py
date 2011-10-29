#!/usr/bin/env python
# coding: utf-8

import unittest
from csv import CSV

class TestCSV(unittest.TestCase):

    def test_if_there_are_3_fields(self):
        csv=CSV()
        self.assertEquals(len(csv.fields), 3)

if __name__ == '__main__':
    unittest.main()