from veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca_moto, modelo_moto, tipo):
        super().__init__(marca_moto, modelo_moto)
        self._tipo = tipo
    
    @property
    def tipo(self):
        return self._tipo
    
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nEstado do veículo: {self.ligado}\nTipo da moto: {self.tipo}\n'

