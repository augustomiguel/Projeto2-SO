#Least Recently Used ou Menos Recentemente Utilizado
from arquivo import Arquivo

class LRU:
    quadros = 0
    processos = []
    processosCopia = []
    faltaDeQuadros = 0
    primeiroInserido = 0
    lista = []
    indice = -1

    def lru(self, arq):
        self.quadros = arq.quadros
        self.processos = arq.processos
        self.processosCopia = arq.processos
        self.lista = [None]*self.quadros
        
        while self.processos:
            processoAtual = self.processos[0]
            self.processos.remove(processoAtual)
        
            if processoAtual not in self.lista:
                self.porNaLista(processoAtual)
                
                      

        
    def porNaLista(self,processoAtual):
        
        if None in self.lista :
            for j in range(len(self.lista)):
                if self.lista[j] == None:
                    self.lista[j] = processoAtual
                    self.indice += 1 
                    break
        else:
            
            if self.primeiroInserido < self.quadros: 
                
                self.lista[self.primeiroInserido] = processoAtual
                self.faltaDeQuadros += 1 
                self.primeiroInserido += 1
                print("falta de quadros",self.faltaDeQuadros)
                
            else:
                self.primeiroInserido = 0
                self.lista[self.primeiroInserido] = processoAtual  
                self.faltaDeQuadros += 1 
                print("falta de quadros tres ",self.faltaDeQuadros) 
            
    def buscarIndice(self, processoAtual ):
        i = self.indice
        j = 0
        k = 0
        vetor[]
        while i != -1: #and j <= self.quadros :
            #if self.lista[j] == self.processosCopia[i]:
            for j in range(self.quadros)
                if self.processosCopia[i] == self.lista[j]
                    vetor.append(j)
            j += 1
            
            

            i -= 1 
            
        
                
                        
                
#arq = Arquivo()
#arq.extrairProcessos("processos.txt")       
fi=LRU()
fi.lru()
#print("falta de quadros",fi.faltaDeQuadros) 
#print(fi.faltaDeQuadros)
