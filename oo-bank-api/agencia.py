from banco import Banco

class Agencia(Banco):
    def __init__(self, nome_agencia, endereco_agencia, numero_agencia):
        super().__init__(nome_agencia, endereco_agencia)
        self._numero = numero_agencia