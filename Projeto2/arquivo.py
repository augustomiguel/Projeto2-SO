
class Arquivo:
  quadros = None
  processos = []

  def lerArquivo(self, nomeArq):
    try:
      with open(nomeArq, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()
            self.extrairProcessos(linhas)
    except FileNotFoundError:
      print(f"Erro: Arquivo '{nomeArq}' não encontrado.")
      exit(1)
    except Exception as e:
      print(f"Erro ao abrir arquivo '{nomeArq}': {e}")
      exit(1)

  def extrairProcessos(self, linhas):

    for linha in linhas:
      aux = linha.strip()
      self.processos.append(int(aux))
      #print("aux",aux)
    self.quadros = (self.processos[0])
    #print("quadros",self.quadros)
    self.processos.remove(self.processos[0])


#arq = Arquivo()
#arq.lerArquivo("processos.txt")
#print(arq.processos)
