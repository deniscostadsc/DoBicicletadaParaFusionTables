## Do Bicicletada para o Fusion Tables

Projeto puramente didático que tem como objetivo plotar em um mapa do Google Maps a localização dos grupos cadastrados no http://www.bicicletada.org.

Para isso será feito um parsing do html do menu do site e gerado um CSV a partir dessas informações.

Este CSV será então postado no Fusion Tables, e este gerará a geolocalização no mapa.

### Arquivos

O diretório *randomfile* tem os arquivos html(do index do bibicletada.org), kml e csv.

### Fusion Tables do projeto

http://www.google.com/fusiontables/DataSource?dsrcid=2008382

### Testes

Para executar os testes das classes, execute o seguinte comando

    $ python teste_classe.py
