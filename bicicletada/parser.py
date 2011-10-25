# coding: utf-8

import re

file = open('index.html', 'r')
content = file.read()
ver = ''
string = ''
for line in content.split('\n'):
    if line.startswith('<div id="Estados"'):
        ver = True
    if line.startswith('</div>') and ver == True:
        ver = False
    if ver == True:
        string = string + line
    if ver == False:
        break

string = string.replace('<a href="">', '\n')
string = re.sub('<[^>]*>', ' ', string)
string = re.sub('Adicione sua cidade', '', string)

#print(string)

for line in string.splitlines():
    print(line)