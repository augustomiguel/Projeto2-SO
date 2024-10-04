#!/usr/bin/env python
# -*- coding: utf-8 -*-

class OTM:
    """Algoritmo Otimo (OTM) para substituicao de paginas na memoria RAM"""

    def execute(self, qtd_quadros, referencias):
        """
        Executa o algoritmo de substituicao de paginas OTM. Recebe como
        parametros a quantidade de quadros e a lista de paginas referenciadas.
        """
        # Inicializa os valores de miss
        miss = 0 # Quando a pagina referenciada nao esta na memoria

        quadros = [] # Quadros da memoria

        # Percorre a lista de paginas referenciadas
        for indice, ref in enumerate(referencias):
            if ref not in quadros:
                miss += 1 # incrementa o numero de paginas faltantes

                if len(quadros) == qtd_quadros:
                    indice_depois = self.__pagina_referenciada_depois(indice, quadros, referencias)
                    quadros.remove(indice_depois)

                quadros.append(ref)

        # Retorna o numero de paginas nao encontradas na memoria RAM
        return miss


    def __pagina_referenciada_depois(self, indice_atual, quadros, referencias):
        """
        Procura a pagina que vai demorar mais para ser referenciada novamente.
        Recebe como parametros o indice da pagina atual, os quadros da memoria
        e a lista de paginas referenciadas.
        """

        # Dicionario para armazenar o numero de referencias ate que uma pagina
        # na memoria seja referenciada novamente
        tempos = {}

        # Percorre as paginas na memoria
        for q in quadros:
            tempos[q] = 0 # inicializa o numero de referencias ate a proxima
            # Busca da referencia atual ate a proxima
            for r in range(indice_atual+1, len(referencias)):
                if referencias[r] != q:
                    tempos[q] += 1 # Incrementa o numero de referencias ate a proxima
                else:
                    break # Para quando encontra a proxima referencia

        # Inicializa a pagina que vai demorar mais a ser referenciadacomo a primeira
        depois = list(tempos.values())[0]
        chave = list(tempos.keys())[0] # Pagina que vai demorar mais para ser referenciada novamente

        # Busca pagina que vai demorar mais para ser referenciada novamente
        for t in list(tempos.keys()):
            if tempos[t] > depois:
                depois = tempos[t]
                chave = t

        # Retorna a pagina que vai demorar mais para ser referenciada novamente
        return chave

otm = OTM()
a = otm.execute(4 ,[1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] )
print(a)
