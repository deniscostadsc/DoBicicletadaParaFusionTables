#coding: utf-8

from page import Page
from parser import Parser

#Cria uma classe "CSV" que monta o csv e dá nome as colunas
class CSV(object):
    #construtor
    def __init__(self):
        self.column_names = ['"Estado"', '"Localização"', '"URL"']
        # cria um objeto da classe parser "t" 
        t = Parser()
        #pega o html e devolve a tabela
        self.csv_table = t.parse()
        #coloca no arquivo csv os nomes das colunas.
        self.csv_table.insert(0, self.column_names)
    
    #Cria um novo arquivo e junta as linhas da tabela CSV quebrando as linhas.
    def save_csv(self, filename='grupos_bicicletada.csv'):
        #"w" para escrever porque se esta criando um novo arq.
        csv_file = open(filename, 'w')
        for line in self.csv_table:
            csv_file.write(','.join(line))
            csv_file.write('\n')
        csv_file.close()
