#!/usr/bin/env python
# coding: utf-8

import unittest
from fusiontables import FusionTables

class TestFusiontables(unittest.TestCase):
    def setUp(self):
        self.fusion = FusionTables()
    
    def test_should_return_teresina_url(self):
        self.assertEquals(self.fusion.sqlquery("SELECT URL FROM 2008382 WHERE Estado = 'Piauí'"),
                                          'URL\nhttp://www.bicicletada.org/Teresina\n')
    
if __name__ == '__main__':
    unittest.main()
