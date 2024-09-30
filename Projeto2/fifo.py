# First In, First Out
from arquivo import Arquivo

class FIFO:
    
    def fifo(self,obj):
        quadros = obj.quadros
        processos = obj.processos
        lista = [None]*int(quadros)
        print(len(lista))
        
        while processos:
            processoAtual = processos[0]
            processos.remove(processoAtual)
            
            for i in range (len(lista)) :
                
                if processoAtual in lista :
                    continue
                elif processoAtual not in lista:
                    for j in range(len(lista)):
                        if lista[j] == None:
                            lista[j] = int(processoAtual)
                            break
                    continue
                
                        
                
arq = Arquivo()
arq.extrairProcessos("processos.txt")       
fi=FIFO()
fi.fifo(arq)