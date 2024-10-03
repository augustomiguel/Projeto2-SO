from arquivo import Arquivo
from fifo import FIFO
from lru import LRU
from otm import OTM

def main ():
    arq = Arquivo()
    arq.extrairProcessos("processos.txt")  

    fifo = FIFO()
    fifo.fifo(arq)
    lru = LRU()
    lru.lru(arq)
    otm = OTM() 
    otm.otm(arq)


main()