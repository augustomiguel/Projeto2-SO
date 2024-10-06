from arquivo import Arquivo
from fifo import FIFO
from lru import LRU
from otm import OTM

def main ():
    arq = Arquivo()
    arq.lerArquivo("processos.txt")  

    fifo = FIFO()
    fifo.fifo(arq)
    lru = LRU()
    lru.lru(arq)

    otm = OTM() 
    otm.otm(arq)
    print("Processos FIFO = {0}, LRU = {1}, OTM = {2} \n".format(fifo.faltaDeQuadros,
                                                                lru.faltaDeQuadros,
                                                                otm.faltaDeQuadros))
    
    arq2 = Arquivo()
    arq2.lerArquivo("processos2.txt") 
    fifo2 = FIFO()
    fifo2.fifo(arq2)
    lru2 = LRU()
    lru2.lru(arq2)
    otm2 = OTM() 
    otm2.otm(arq2)
    print("Processos2 FIFO = {0}, LRU = {1}, OTM = {2} \n ".format(fifo2.faltaDeQuadros,
                                                                    lru2.faltaDeQuadros,
                                                                    otm2.faltaDeQuadros))

    arq3 = Arquivo()
    arq3.lerArquivo("processos3.txt")  
    fifo3 = FIFO()
    fifo3.fifo(arq3)
    lru3 = LRU()
    lru3.lru(arq3)
    otm3 = OTM() 
    otm3.otm(arq3)
    print("Processos3 FIFO = {0}, LRU = {1}, OTM = {2} \n".format(fifo3.faltaDeQuadros,
                                                                lru3.faltaDeQuadros,
                                                                otm3.faltaDeQuadros))
    
    arq4 = Arquivo()
    arq4.lerArquivo("processos4.txt")  
    fifo4 = FIFO()
    fifo4.fifo(arq4)
    lru4 = LRU()
    lru4.lru(arq4)
    otm4 = OTM() 
    otm4.otm(arq)
    print("Processos4 FIFO = {0}, LRU = {1}, OTM = {2} \n".format(fifo4.faltaDeQuadros,
                                                                lru4.faltaDeQuadros,
                                                                otm4.faltaDeQuadros))

main()