# First In, First Out
from arquivo import Arquivo

class FIFO:
    quadros = 0
    processos = []
    faltaDeQuadros = 0
    primeiroInserido = 0
    lista = []

    def fifo(self,arq):
        self.quadros = arq.quadros
        self.processos = arq.processos
        self.lista = [None]*self.quadros
        
        while self.processos :
            processoAtual = self.processos[0]
            self.processos.remove(processoAtual)
            
            #if processoAtual in self.lista :   
            if processoAtual not in self.lista:
                #print("não estou na lista")
                self.porNaLista(processoAtual)
        self.faltaDeQuadros += self.quadros
    

        
    def porNaLista(self,processoAtual):
        
        if None in self.lista :
            for j in range(len(self.lista)):
                if self.lista[j] == None:
                    self.lista[j] = processoAtual
                    break
        else:
            
            if self.primeiroInserido < self.quadros: 
                
                self.lista[self.primeiroInserido] = processoAtual
                self.faltaDeQuadros += 1 
                self.primeiroInserido += 1                
            else:
                self.primeiroInserido = 0
                self.lista[self.primeiroInserido] = processoAtual  
                self.faltaDeQuadros += 1 
                
        


       
            
                
                        
                
arq = Arquivo()
arq.lerArquivo("processos.txt")       
fi=FIFO()
fi.fifo(arq)
print("falta de quadros",fi.faltaDeQuadros) 
#print(fi.faltaDeQuadros)
