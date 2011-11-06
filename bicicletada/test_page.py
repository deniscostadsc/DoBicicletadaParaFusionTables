#!/usr/bin/env python
# coding: utf-8

import unittest
from page import Page

class TestPage(unittest.TestCase):
    def setUp(self):
        self.page = Page()

    def test_if_page_exist(self):
        self.assertEquals(self.page.status_code, 200)
    
    def test_if_content_is_HTML(self):
        self.assertEquals(self.page.content.endswith('</html>'), True)

if __name__ == '__main__':
    unittest.main()
