#coding: utf-8
from bicicletada.csv import CSV
from fusiontables.fusiontables import FusionTables


def main():
    c = CSV()
    c.save_csv()
    c.save_csv('lero-lero.csv')

    f = FusionTables()
    print f.sqlquery("SELECT URL FROM 2008382 WHERE Estado = 'São Paulo'")

if __name__ == '__main__':
    main()
