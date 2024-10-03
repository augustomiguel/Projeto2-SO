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
        self.processosCopia = arq.processos[:]
        #print(self.processosCopia)
        self.lista = [None]*self.quadros
        
        while self.processos:
            processoAtual = self.processos[0]
            self.processos.remove(processoAtual)
        
            if processoAtual in self.lista:
                self.indice += 1
            else :
                self.porNaLista(processoAtual)
            print("lista", self.lista)

    def porNaLista(self,processoAtual):
        
        if None in self.lista :
            for j in range(len(self.lista)):
                if self.lista[j] == None:
                    self.lista[j] = processoAtual
                    self.indice += 1 
                    break
        else:
            self.buscarIndice(processoAtual)                
            
    def buscarIndice(self, processoAtual ):
        i = self.indice
        j = 0
        vetor = []
        #print(self.processosCopia)
        
        while i > -1: #and j <= self.quadros :

            if len(vetor) == len(self.lista):
                break

            for j in range(len(self.lista) - 1 ):
               
                if self.processosCopia[i] == self.lista[j]:
                    vetor.append(j)
                    break
                    
                j += 1                            
                
            i -= 1 
        self.inserir(vetor, processoAtual) 


    def inserir(self, vetor , processoAtual):
        self.lista[len(vetor)-1] = processoAtual
        self.faltaDeQuadros += 1

        

arq = Arquivo()
arq.lerArquivo("processos.txt")       
fi=LRU()
fi.lru(arq)
print("falta de quadros",fi.faltaDeQuadros) 
