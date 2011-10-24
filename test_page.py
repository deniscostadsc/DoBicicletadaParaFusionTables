#!/usr/bin/env python
# coding: utf-8

import unittest
from page import Page
from page import CSV

class TestPage(unittest.TestCase):

    def test_if_page_exist(self):
        page=Page()
        self.assertEquals(page.status_code, 200)
    
    def test_if_content_is_HTML(self):
        page=Page()
        self.assertEquals(page.content.endswith('</html>'), True)

class TestCSV(unittest.TestCase):

    def test_if_there_are_3_fields(self):
        csv=CSV()
        self.assertEquals(len(csv.fields), 3)

if __name__ == '__main__':
    unittest.main()