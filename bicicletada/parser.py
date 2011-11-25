# coding: utf-8

import re #biblioteca
from page import Page

class Parser(object):
    def __init__(self):
        #Atributos
        self.page = Page()
        self.content = self.page.content

    #pega todos os nomes de estados e cidades que encontram-se no menu do site bicicletada.
    #método
    def parse(self):
        #file = open('index.html', 'r')
        #content = file.read()
        
        # Pegando a linha do menu
        for line_file in self.content.split('\n'):
            if 'cssmenu0' in line_file:
                str1 = line_file
                break

        # Pegando cidades e estados
        str1 = str1.replace(r'<a href="">', '\n')
        str2 = str1
        str1 = re.sub(r'<[^>]*>', ' ', str1)
        str1 = re.sub(r' *Adicione sua cidade *', '', str1)
        lines = re.sub(r'  +', ',', str1).splitlines()

        # Pegando urls
        str2 = re.sub(r'<[^a][^>]*>', '', str2)
        str2 = re.sub(r'[^"]*"([\w0-9+%]+)"[^"]*', r'\1,', str2)
        str2 = re.sub(r'"tiki-index.php\?page=Aracaju"', r'Aracaju,', str2)
        str2 = re.sub(r',Adicione\+sua\+cidade,', r'', str2)
        urls = re.sub(r'"\(?\((\w+)\)"', r'\1,', str2).split(',')

        # Montando a tabela
        table = []
        cont = 0
        for line in lines:
            if line != '':
                l = line.split(',')
                state = l[0].strip()
                for city in l[1:]:
                    if city != '':
                        location = '%s, %s' % (city, state)
                        table.append(['"%s"' % state,
                                      '"%s"' % location,
                                      '"%s"' % ('http://www.bicicletada.org/' +  urls[cont])])
                        cont += 1
        return table
