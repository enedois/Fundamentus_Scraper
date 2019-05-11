from urllib.request import urlopen
import os
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

## cria diretorio para a data de hoje-1
os.mkdir(data)


url = "http://fundamentus.com.br/detalhes.php?papel="

def faltam(papeis):
    print(len(papeis))

while len(papeis)>0:
    for papel in papeis:                 
            try:
                    content = urlopen(url+papel)
                    #print(papel+": "+str(content.code))
                    html = content.read()
                    # print (html)
                    
                    if(b'Nenhum papel encontrado' in html):
                            print(papel+ "-> Inválido")
                            #retira o papel do array
                            popvalue = papeis.index(papel)
                            papeis.pop(popvalue)
                            faltam(papeis)
                    else:
                            print(papel+ "-> Válido")
                            file = open(data+"/"+papel+'.html','wb')
                            file.write(html)
                            print(papel+ "-> Gravado")
                            file.close()
                            print(papel+ "-> Terminado")
                            #retira o papel do array
                            popvalue = papeis.index(papel)
                            papeis.pop(popvalue)
                            faltam(papeis)
            except:
                    print("### Erro: "+papel)
                    #print(papeis)


