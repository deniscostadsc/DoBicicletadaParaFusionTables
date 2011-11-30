#!/usr/bin/env python
# coding: utf-8

import urllib
#Toda classe herda de Object ou herda de outras classes que herdam de object
class Page(object):

    #self indica que o atributo é do objeto, sem self é da classe    
    def __init__(self):        
        self.__url='http://bicicletada.org/'

        # Pega a página configurada na URL.
        page=urllib.urlopen(self.__url)

        # Retorna código de retorno HTTP
        # mais informação em:
        # http://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol#C.C3.B3digos_de_retorno
        self.__status_code=page.getcode()

        # Joga o conteúdo da página nesse atributo.
        self.__content=page.read()
        
        page.close()

    @property
    def url(self):
        return self.__url
    
    @property
    def status_code(self):
        return self.__status_code

    @property
    def content(self):
        return self.__content
