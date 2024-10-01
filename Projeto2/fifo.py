# First In, First Out
from arquivo import Arquivo

class FIFO:
    quadros = 0
    processos = []
    faltaDeQuadros = 0
    primeiroInserido = 0
    lista = []

    def fifo(self):
        self.quadros = 4 #/obj.quadros
        self.processos = [1,2,3,4,1,2,5,1,2,3,4,5]
        self.lista = [None]*self.quadros
        
        while self.processos:
            processoAtual = self.processos[0]
            self.processos.remove(processoAtual)
            
            #if processoAtual in self.lista :   
            if processoAtual not in self.lista:
                #print("não estou na lista")
                self.porNaLista(processoAtual)
                
                      

        
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
                print("falta de quadros",self.faltaDeQuadros)
                
            else:
                self.primeiroInserido = 0
                self.lista[self.primeiroInserido] = processoAtual  
                self.faltaDeQuadros += 1 
                print("falta de quadros tres ",self.faltaDeQuadros)
        

#
       
            
                
                        
                
#arq = Arquivo()
#arq.extrairProcessos("processos.txt")       
fi=FIFO()
fi.fifo()
#print("falta de quadros",fi.faltaDeQuadros) 
#print(fi.faltaDeQuadros)