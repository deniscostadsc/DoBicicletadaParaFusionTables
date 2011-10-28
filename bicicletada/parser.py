# coding: utf-8

import re

file = open('index.html', 'r')
content = file.read()
for line_file in content.split('\n'):
    if 'cssmenu0' in line_file:
        str1 = line_file
        break

# Pegando cidades e estados
str1 = str1.replace(r'<a href="">', '\n')
str2 = str1
str1 = re.sub(r'<[^>]*>', ' ', str1)
str1 = re.sub(r' *Adicione sua cidade *', '', str1)
str1 = re.sub(r'  +', ',', str1)

# Pegando urls
str2 = re.sub(r'<[^a][^>]*>', '', str2)
str2 = re.sub(r'[^"]*"([\w0-9+%]+)"[^"]*', r'\1,', str2)
str2 = re.sub(r'"tiki-index.php\?page=Aracaju"', r'Aracaju,', str2)
str2 = re.sub(r',Adicione\+sua\+cidade,', r'', str2)
str2 = re.sub(r'"\(\(PontaGrossa\)"', r'PontaGrossa,', str2)
urls = re.sub(r'"\(SantoAndre\)"', r'SantoAndre,', str2).split(',')


#print(len(urls))

lines = str1.splitlines()

table = []

cont = 0
for line in lines:
    if line != '':
        l = line.split(',')
        state = l[0].strip()
        for city in l[1:]:
            if city != '':
                location = '%s, %s' % (city, state)
                table.append([state, location, 'http://www.bicicletada.org/' + urls[cont]])
                cont += 1

cont = 0
for line in table:
    for i in line:
        print(i)
    cont += 1

#print(cont)
