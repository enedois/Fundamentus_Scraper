from urllib.request import urlopen
import os
#from pyquery import PyQuery as pq
from lxml import etree
papeis = [
"AALR3",
"ABCB4",
"ABCP11",
"ABEV3",
"ADHM3",
"AEFI11",
"AGCX11",
"AGRO3",
"ALMI11",
"ALPA3",
"ALPA4",
"ALSC3",
"ALUP11",
"ALZR11",
"AMAR3",
"ANIM3",
"APER3",
"ARZZ3",
"AZUL4",
"B3SA3",
"BAHI3",
"BBAS3",
"BBDC3",
"BBDC4",
"BBFI11B",
"BBPO11",
"BBRC11",
"BBRK3",
"BBSE3",
"BBVJ11",
"BCFF11",
"BCIA11",
"BCRI11",
"BEEF3",
"BGIP4",
"BIDI4",
"BIOM3",
"BKBR3",
"BMLC11B",
"BPAC11",
"BPAN4",
"BPFF11",
"BRAP3",
"BRAP4",
"BRCR11",
"BRDT3",
"BRFS3",
"BRKM3",
"BRKM5",
"BRML3",
"BRPR3",
"BRSR3",
"BRSR6",
"BSEV3",
"BTOW3",
"CAMB4",
"CAML3",
"CARD3",
"CARE11",
"CBOP11",
"CCPR3",
"CCRO3",
"CCXC3",
"CEDO4",
"CEOC11",
"CESP3",
"CESP6",
"CGRA3",
"CGRA4",
"CIEL3",
"CLSC4",
"CMIG3",
"CMIG4",
"CNES11",
"COCE5",
"CPFE3",
"CPLE3",
"CPLE6",
"CPRE3",
"CPTS11B",
"CRDE3",
"CRFB3",
"CSAN3",
"CSMG3",
"CSNA3",
"CTNM4",
"CTXT11",
"CVCB3",
"CXCE11B",
"CXRI11",
"CYRE3",
"DASA3",
"DIRR3",
"DMMO3",
"DTEX3",
"ECOR3",
"EDGA11",
"EGIE3",
"ELEK4",
"ELET3",
"ELET6",
"ELPL3",
"EMBR3",
"ENBR3",
"ENEV3",
"ENGI11",
"EQTL3",
"ESTC3",
"EUCA4",
"EURO11",
"EVEN3",
"EZTC3",
"FAED11",
"FAMB11B",
"FCFL11",
"FESA4",
"FEXC11",
"FFCI11",
"FIGS11",
"FIIB11",
"FIIP11B",
"FIXX11",
"FJTA3",
"FJTA4",
"FLMA11",
"FLRY3",
"FOFT11",
"FRAS3",
"FRIO3",
"FVBI11",
"GEPA4",
"GFSA3",
"GGBR3",
"GGBR4",
"GGRC11",
"GNDI3",
"GOAU3",
"GOAU4",
"GOLL4",
"GRLV11",
"GRND3",
"GSHP3",
"GUAR3",
"HAPV3",
"HBOR3",
"HCRI11",
"HFOF11",
"HGBS11",
"HGCR11",
"HGJH11",
"HGLG11",
"HGRE11",
"HGRU11",
"HGTX3",
"HTMX11",
"HYPE3",
"IDVL3",
"IGTA3",
"IRBR3",
"IRDM11",
"ITSA3",
"ITSA4",
"ITUB3",
"ITUB4",
"JBSS3",
"JFEN3",
"JHSF3",
"JRDM11",
"JSLG3",
"JSRE11",
"KEPL3",
"KLBN11",
"KNCR11",
"KNHY11",
"KNIP11",
"KNRE11",
"KNRI11",
"KROT3",
"LAME3",
"LAME4",
"LCAM3",
"LEVE3",
"LIGT3",
"LINX3",
"LIQO3",
"LLIS3",
"LOGG3",
"LOGN3",
"LPSB3",
"LREN3",
"MALL11",
"MAXR11",
"MBRF11",
"MDIA3",
"MEAL3",
"MFII11",
"MGFF11",
"MGLU3",
"MILS3",
"MOVI3",
"MPLU3",
"MRFG3",
"MRVE3",
"MULT3",
"MXRF11",
"MYPK3",
"NATU3",
"NSLU11",
"ODPV3",
"OFSA3",
"OMGE3",
"ONEF11",
"OUJP11",
"PARD3",
"PCAR4",
"PETR3",
"PETR4",
"PFRM3",
"PINE4",
"PMAM3",
"POMO3",
"POMO4",
"PORD11",
"POSI3",
"PQDP11",
"PRIO3",
"PSSA3",
"PTBL3",
"PTNT4",
"QGEP3",
"QUAL3",
"RADL3",
"RAIL3",
"RAPT3",
"RAPT4",
"RBBV11",
"RBGS11",
"RBRD11",
"RBRF11",
"RBRR11",
"RDNI3",
"RENT3",
"RLOG3",
"RNDP11",
"RNEW11",
"RNEW3",
"RNEW4",
"RNGO11",
"ROMI3",
"RSID3",
"SAAG11",
"SANB11",
"SAPR11",
"SAPR4",
"SBSP3",
"SCAR3",
"SDIL11",
"SEDU3",
"SEER3",
"SGPS3",
"SHOW3",
"SHPH11",
"SLCE3",
"SMLS3",
"SMTO3",
"SPTW11",
"SQIA3",
"SSBR3",
"STBP3",
"SULA11",
"SUZB3",
"TAEE11",
"TBOF11",
"TCSA3",
"TECN3",
"TEND3",
"TESA3",
"TGAR11",
"TGMA3",
"THRA11",
"TIET11",
"TIMP3",
"TOTS3",
"TRIS3",
"TRPL4",
"TRPN3",
"TRXL11",
"TUPY3",
"UBSR11",
"UCAS3",
"UGPA3",
"UNIP6",
"USIM3",
"USIM5",
"VALE3",
"VISC11",
"VIVT4",
"VLID3",
"VLOL11",
"VRTA11",
"VULC3",
"VVAR3",
"WEGE3",
"WIZS3",
"XPCM11",
"XPLG11",
"XPML11",
"XTED11"]
url = "http://fundamentus.com.br/detalhes.php?papel="
while len(papeis)>0:
    for papel in papeis:
            #print(os.getcwd())
            #print("Fetching: "+papel)
       
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
                    else:
                            print(papel+ "-> Válido")
                            file = open(papel+'.html','wb')
                            file.write(html)
                            print(papel+ "-> Gravado")
                            file.close()
                            print(papel+ "-> Terminado")
                            #retira o papel do array
                            popvalue = papeis.index(papel)
                            papeis.pop(popvalue)
            except:
                    print("### Erro: "+papel)
                    print(papeis)
