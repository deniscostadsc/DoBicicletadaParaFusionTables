#coding: utf-8

import urllib2
import urllib
from getpass import getpass

class Google(object):
    def googlelogin(self, service):
        login = raw_input('Login: ')
        password = getpass('Password: ')
        url_login = 'https://www.google.com/accounts/ClientLogin?'
        uri = urllib.urlencode({'Email': login, 'Passwd': password, 'service': service})
        p = urllib.urlopen(url_login + uri).read()

        for line in p.splitlines():
            if line.startswith('Auth='):
                auth_token = line.replace('Auth=', '')
        return auth_token

class FusionTables(Google):
    def sqlquery(self, query):
        token = self.googlelogin('fusiontables')
        header = {'Authorization': 'GoogleLogin auth=%s' % token}
        encoded_query = urllib.urlencode({'sql': query})
        p = urllib2.Request('https://www.google.com/fusiontables/api/query?%s' % encoded_query, headers=header)
        content = urllib2.urlopen(p).read()
        return content
