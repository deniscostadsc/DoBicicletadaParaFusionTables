import urllib

class Page(object):

    def __init__(self):
        self.url='http://bicicletada.org/'

        # Pega a página configurada na URL.
        self.page=urllib.urlopen(self.url)

        # Retorna código de retorno HTTP
        # mais informação em:
        # http://pt.wikipedia.org/wiki/Hypertext_Transfer_Protocol#C.C3.B3digos_de_retorno
        self.status_code=self.page.getcode()

        # Joga o conteúdo da página nesse atributo.
        self.content=self.page.read()
        
        self.page.close()

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

