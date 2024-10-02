void simula_lru(struct memoria mem) {
  int faltas = 0;
  int i = 0, j = 0, k = 0, l = 0;

  int *quadros = (int *)malloc(mem.qtd_quadros * sizeof(int));
  int *aux = (int *)malloc(mem.qtd_quadros * sizeof(int)); 

  if (quadros == NULL || aux == NULL) {
    perror("Erro ao alocar memória para quadros.\nEncerrando...\n");
    exit(1);
  }

  // Inicializando quadros
  for(i = 0; i < mem.qtd_quadros; i++) { quadros[i] = -1; }

  // Percorrendo referências às memórias, adicionando aos quadros e contando faltas de páginas
  for(i = 0; i < mem.qtd_referencias; i++) {
    int pagina_na_memoria = 0;
    int fluxo_paginas = 0; // página atual foi inserida nos quadros ou uma página foi substituída durante este ciclo

    // Verifica se a página atual sendo referenciada existe na memória (quadros)
    for (j = 0; j < mem.qtd_quadros; j++) {
      if (quadros[j] == mem.referencias[i]) {
        pagina_na_memoria = 1;
        fluxo_paginas = 1;
        break;
      }
    }

    // Caso a página não esteja na memória...
    if (pagina_na_memoria == 0) {
      for (j = 0; j < mem.qtd_quadros; j++) {
        if(quadros[j] == -1) {
          quadros[j] = mem.referencias[i];
          fluxo_paginas = 1;
          faltas++;
          break;
        }
      }
    }

    // Caso a página atual tenha sido inserida ou uma página foi substituída no fluxo
    if(fluxo_paginas == 0) {
      for(j = 0; j < mem.qtd_quadros; j++) {
        aux[j] = 0;
      }

      // Preenchendo aux com 1 para quando a referencia passada estiver no quadro
      for(k = i - 1, l = 1; l <= mem.qtd_quadros - 1; l++, k--) {
        for(j = 0; j < mem.qtd_quadros; j++) {
          if(quadros[j] == mem.referencias[k]) {
            aux[j] = 1;
          }
        }
      }

      // Caso algum índice de aux tenha ficado como zero, essa posição é salva
      int posicao = 0;
      for(j = 0; j < mem.qtd_quadros; j++) {
        if(aux[j] == 0) {
          posicao = j;
          break;
        }
      }
      // substituindo coonteúdo do quadro e contabilizando falta de página
      quadros[posicao] = mem.referencias[i];
      faltas++;
    }
  }

  printf("LRU %d\n", faltas); 

  // libera a memória alocada
  free(quadros); 
  free(aux);
}