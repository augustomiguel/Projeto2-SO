# Algoritmo Ótimo

from arquivo import Arquivo

class OTM:
    quadros = 0
    processos = []
    processosCopia = []
    faltaDeQuadros = 0
    primeiroInserido = 0
    lista = []
    indice = 0

    def otm(self, arq):
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
        i = self.indice + 1
        j = 0
        vetor = []
        
        while i < len(self.processosCopia): 

            for j in range(len(self.lista)): #tirei o -1
               
                if self.processosCopia[i] == self.lista[j]:
                    if j not in vetor:
                        vetor.append(j)
                        break
                j += 1
                                        
                
            i += 1 
           
        self.inserir(vetor, processoAtual) 


    def inserir(self, vetor, processoAtual):
        
        if len(vetor) < self.quadros:
            i = 0
            for i in range(self.quadros):
                
                if i not in vetor:
                    localInsercao = i    
                    break
                
            self.lista[localInsercao] = processoAtual
            #print("inserção = ", self.lista)
            self.faltaDeQuadros += 1
            self.indice += 1  
        
        elif len(vetor) == 0:
            
            self.lista[0] = processoAtual
            #print("inserção = ", self.lista)
            self.faltaDeQuadros += 1
            
        else:

            localInsercao = vetor[len(vetor) - 1]
            self.lista[localInsercao] = processoAtual
            #print("inserção = ", self.lista)
            self.faltaDeQuadros += 1
            self.indice += 1 
            
        
            
        

        

# arq = Arquivo()
# arq.lerArquivo("processos4.txt")       
# fi=OTM()
# fi.otm(arq)
# print("falta de quadros",fi.faltaDeQuadros)