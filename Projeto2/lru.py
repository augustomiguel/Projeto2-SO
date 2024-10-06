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
        self.lista = [None]*self.quadros
        
        while self.processos:
            processoAtual = self.processos[0]
            self.processos.remove(processoAtual)
        
            if processoAtual in self.lista:
                self.indice += 1
            else :
                self.porNaLista(processoAtual)
                
        self.faltaDeQuadros += self.quadros
        #print("falta de quadros lru", self.faltaDeQuadros)
        #return print("terminei lru")
        
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
   
        while i > -1: 

            for j in range(len(self.lista)): #tirei o -1
               
                if self.processosCopia[i] == self.lista[j]:
                    if j not in vetor:
                        vetor.append(j)
                        break
                j += 1
                                        
                
            i -= 1 
            
        self.inserir(vetor, processoAtual) 


    def inserir(self, vetor, processoAtual):
        localInsercao = vetor[len(vetor) - 1 ]
        self.lista[localInsercao] = processoAtual
        #print("inserção = ", self.lista)
        self.faltaDeQuadros += 1
        self.indice += 1 #faltava somar o indice aqui 
        

        

arq = Arquivo()
arq.lerArquivo("processos.txt")       
fi=LRU()
fi.lru(arq)
print("falta de quadros1 =",fi.faltaDeQuadros) 

arq2 = Arquivo()
arq2.lerArquivo("processos2.txt")       
fi=LRU()
fi.lru(arq2)
print("falta de quadros2 =",fi.faltaDeQuadros) 

arq3 = Arquivo()
arq3.lerArquivo("processos3.txt")       
fi=LRU()
fi.lru(arq3)
print("falta de quadros3 =",fi.faltaDeQuadros) 


arq4 = Arquivo()
arq4.lerArquivo("processos4.txt")       
fi=LRU()
fi.lru(arq4)
print("falta de quadros4 =",fi.faltaDeQuadros) 