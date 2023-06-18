class Pessoa:
  def __init__(self, nome, identificador) -> None:
    self.nome = nome
    self.identificador = identificador

  def __str__(self):
    return f'nome: {self.nome}'
  

  