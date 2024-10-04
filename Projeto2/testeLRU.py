#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
class LRU:
    """Algoritmo Least Recently Used (LRU) para substituicao de paginas na memoria RAM"""

    def execute(self, qtd_quadros, referencias):
        """
        Executa o algoritmo de substituicao de paginas LRU. Recebe como
        parametros a quantidade de quadros e a lista de paginas referenciadas.
        """
        # Inicializa os valores de miss
        miss = 0 # Quando a pagina referenciada nao esta na memoria

        # Configura o instante inicial como zero
        instante = 0

        # Quadros da memoria
        quadros = {} # As chaves sao as paginas e os valores o instante que entrou na memoria

        # Percorre a lista de paginas referenciadas
        for ref in referencias:
            if ref not in list(quadros.keys()):
                miss += 1 # incrementa o numero de paginas faltantes

                # Se todos os quadros estiverem ocupados remove a pagina usada a mais tempo
                if len(quadros) == qtd_quadros:
                    mais_antiga = self.__pagina_mais_antiga(quadros)
                    del quadros[mais_antiga] # Retira a pagina da memoria RAM

            # Adiciona a pagina na memoria RAM ou atualiza o instante de utilizacao
            quadros[ref] = instante
            instante += 1

        # Retorna o numero de paginas nao encontradas na memoria RAM
        return miss


    def __pagina_mais_antiga(self, quadros):
        """
        Procura a pagina referenciada a mais tempo na memoria RAM. Recebe como
        parametros os quadros da memoria.
        """

        # Considera inicialmente a primeira a mais antiga
        mais_antiga = list(quadros.keys())[0]
        menor_instante = list(quadros.values())[0]

        # Compara os instantes da ultima utilizacao de cada pagina
        for chave in list(quadros.keys()):
            # Se chave for menor que a chame da mais antiga ate o momento
            # a mais antiga e atualizada
            if quadros[chave] < menor_instante:
                mais_antiga = chave
                menor_instante = quadros[chave]

        # Retorna a chave da pagina referenciada a mais tempo
        return mais_antiga

lru = LRU()
a = lru.execute(4 ,[1, 2, 3, 4, 1, 2, 5, 1, 2, 3, 4, 5] )
print(a)
