from abc import ABC, abstractmethod

class Veiculo:
    def __init__(self, marca, modelo):
        self._marca = marca
        self._modelo = modelo
        self._ligado = False

    @property
    def ligado(self):
        return 'Ligado' if self._ligado else 'Desligado'
    
    @property
    def marca(self):
        return self._marca
    
    @property
    def modelo(self):
        return self._modelo
    
    def __str__(self):
        return f'Marca: {self.marca}\nModelo: {self.modelo}\nEstado do veículo: {self.ligado}\n'
    
    @abstractmethod
    def ligar():
        pass