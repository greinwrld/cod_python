class ArquivoTexto(object):

  def __init__(self, arquivo: str):
    self.arquivo = arquivo
    self.conteudo = self.extrair_conteudo(arquivo)

  def extrair_conteudo(self, arquivo):
    with open(arquivo, 'r') as file:
        conteudo = file.read()
    return conteudo

  def extrair_linha(self, arquivo, numero_linha: int):
    with open(arquivo, 'r') as file:
        conteudo = file.read()
    lista_com_vazios = conteudo.split(sep='\n')
    lista_sem_vazios = [item for item in lista_com_vazios if item]
    extrair_linha = lista_sem_vazios[numero_linha]
    return extrair_linha
