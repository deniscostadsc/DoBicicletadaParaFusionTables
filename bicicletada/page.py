#!/usr/bin/env python
# coding: utf-8

import urllib
#Toda classe herda de Object ou herda de outras classes que herdam de object
class Page(object):

    #self indica que o atributo é do objeto, sem self é da classe    
    def __init__(self):        
        self.url='http://bicicletada.org/'

        # Pega a página configurada na URL.
        page=urllib.urlopen(self.url)

        # Retorna código de retorno HTTP
        # mais informação em:
        # http://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol#C.C3.B3digos_de_retorno
        self.status_code=page.getcode()

        # Joga o conteúdo da página nesse atributo.
        self.content=page.read()
        
        page.close()
