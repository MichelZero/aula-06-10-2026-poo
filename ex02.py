# autor: Michel
# data: 06/10/2026

class Teste:
  def __init__(self, nome):
    self._nome = nome
    
  @property
  def nome(self):
    return self._nome
  
  @nome.setter
  def nome(self, valor):
      self._nome = valor