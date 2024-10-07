from arquivo import Arquivo
from fifo import FIFO
from lru import LRU
from otm import OTM
import copy

def main ():
    arq = Arquivo()
    arq.lerArquivo("processos4.txt")  

    fifo = FIFO()
    fifo.fifo(copy.deepcopy(arq))
    print("FIFO",fifo.faltaDeQuadros)
    
    otm = OTM()
    otm.otm(copy.deepcopy(arq))
    print("OTM ",otm.faltaDeQuadros)
    
    lru = LRU()
    lru.lru(copy.deepcopy(arq))
    print("LRU ",lru.faltaDeQuadros)
    

if __name__ == "__main__":
    main()