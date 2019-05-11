import os
from pyquery import PyQuery as pq
import lxml, lxml.html
import datetime

##carrega os papeis de stocksList.csv
stocksList = open('stocksList.csv', 'r')
papeis = stocksList.read().split(';')
stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)

current_dir = os.path.dirname(__file__)
rel_path = data

for papel in papeis:
    try:
        #abrindo o arquivo do papel.html
        arquivo = os.path.join(current_dir, rel_path+"\\"+papel+'.html')
        print(arquivo)     

        ##fazendo o scrap no arquivo do papel.html
        conteudo = pq(filename=arquivo)
        resultado = conteudo("td.data span")
        print(len(resultado))

        #escrevendo os resultados em data.mes
        file = open(data+'.html','ab')
        ##file.write(bytes("<tr>", 'utf-8'))
        for i in resultado:
            conteudo = lxml.html.tostring(i)
            ##file.write(bytes("@", 'utf-8'))
            file.write(conteudo)
            file.write(bytes("@", 'utf-8'))
        ##file.write(bytes("</tr>", 'utf-8'))    
        file.write(bytes("<br/>", 'utf-8'))      
        file.close()
    except:
       print("Erro: "+papel)
