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
    
    def test_if_content_is_not_about_a_error(self):
        page=Page()
        self.assertEquals(page.content.find('<span>Erro</span></div><div class="rbox-data">Página não encontrada <br />'), -1)

class TestCSV(unittest.TestCase):

    def test_if_there_are_3_fields(self):
        csv=CSV()
        self.assertEquals(len(csv.fields), 3)

if __name__ == '__main__':
    unittest.main()