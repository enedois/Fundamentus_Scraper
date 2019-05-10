import os
from pyquery import PyQuery as pq
import lxml, lxml.html

def readFile(filename):
    filehandler = open(filename)
    print (filehandler.read())
    filehandler.close()

current_dir = os.path.dirname(__file__)
rel_path = "TESTE"
papel = "ITSA4"

arquivo = os.path.join(current_dir, rel_path+"\\"+papel+'.html')
print(arquivo)
##readFile(filename) ## para ler o conteudo
conteudo = pq(filename=arquivo)
resultado = conteudo("td.data span")
print(type(resultado))
file = open(papel+'.html','ab')
for i in resultado:
      conteudoString = lxml.html.tostring(i)
      novalinha = bytes("<br/>", 'utf-8')
      file.write(novalinha)
      file.write(conteudoString)
      print(conteudoString)
file.close()
    


