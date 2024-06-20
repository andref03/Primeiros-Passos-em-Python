# importando a Classe Mãe
from banco import Banco

# a Classe Mãe fica entre parênteses
class Agencia(Banco):
    def __init__(self, nome_agencia, endereco_agencia, numero_agencia):
        # método super() faz acessar tudo aquilo que está dentro da Classe Mãe
        super().__init__(nome_agencia, endereco_agencia)
        # a linha abaixo representa um atributo próprio da Classe Filha
        self._numero_agencia = numero_agencia