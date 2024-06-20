from veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca_carro, modelo_carro, qtdd_portas_carro, cor_carro):
        super().__init__(marca_carro, modelo_carro)
        self._qtdd_portas_carro = qtdd_portas_carro
        self._cor_carro = cor_carro
    
    @property
    def qtdd_portas_carro(self):
        return self._qtdd_portas_carro
    
    @property
    def cor_carro(self):
        return self._cor_carro
    
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nEstado do veículo: {self.ligado}\nQtdd de portas do carro: {self.qtdd_portas_carro}\nCor do carro: {self.cor_carro}\n'

    
    def ligar(self):
        self._ligado = True

