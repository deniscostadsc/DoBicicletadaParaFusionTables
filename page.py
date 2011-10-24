import urllib

class Page(object):

    def __init__(self):
        self.url='http://bicicletada.org/'
        self.page=urllib.urlopen(self.url)
        self.status_code=self.page.getcode()
        self.content=self.page.read()
        
        self.page.close()

    def statuscode(self):
        return self.status_code

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

