from urllib.request import urlopen, Request
import os
import datetime

##carrega os papeis de stocksList.csv
stocksList = open('stocksList_old.csv', 'r')
papeis = stocksList.read().split(';')
stocksList.close()

## pegando o dia e mês
now = datetime.datetime.now()
dia = now.day-1
mes = now.month
data = str(dia)+"."+str(mes)

## cria diretorio para a data de hoje-1
if (not os.path.isdir('./'+data)):
    os.mkdir(data)


url = "https://fundamentus.com.br/detalhes.php?papel="

def faltam(papeis):
    print(len(papeis))

while len(papeis)>0:
    for papel in papeis:                 
            try:
                    
                    #print(papel+": "+str(content.code))
                    r = Request(url+papel, headers={'User-Agent': 'Mozilla/5.0'})
                    html = urlopen(r).read()
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
            except Exception as e:
                    print("#ERRO: ",papel," ", str(e))
                    #print(papeis)


