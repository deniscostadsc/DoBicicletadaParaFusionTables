#!/usr/bin/env python
# coding: utf-8

import unittest
from fusiontables import FusionTables

class TestFusiontables(unittest.TestCase):
    def test_should_return_teresina_url(self):
        fusion = FusionTables()
        self.assertEquals(fusion.sqlquery("SELECT URL FROM 2008382 WHERE Estado = 'Piauí'").replace('URL', '').strip(),
                          'http://www.bicicletada.org/Teresina')

if __name__ == '__main__':
    unittest.main()
