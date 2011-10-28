from page import Page

class CSV(object):
    def __init__(self):
        self.fields = ['Localização', 'Estado', 'URL']
    
    # ver = ''
    # for linha in s.split('\n'):
    #     if linha.startswith('<div id="Estados"'):
    #         ver = True
    #     if linha.startswith('</div>') and ver == True:
    #         ver = False
    #     if ver == True:
    #         print(linha)
    #     if ver == False:
    #         break
