from carro import Carro
from moto import Moto

# Criando instâncias
## Carros
carro_001 = Carro('Fiat', 'Kwid', 4)
carro_003 = Carro('Renault', 'Sandero', 4)
carro_002 = Carro('Ford', 'Ka Sedan', 4)
## Motos
moto_001 = Moto('Yamaha', 'XT 3.000', 'Casual')
moto_002 = Moto('Yamaha', 'XLR 8', 'Casual')
moto_003 = Moto('General Motors - GM', 'MotoCross', 'Esportiva')

def main():
    print(carro_001)
    print(carro_002)
    print(carro_003)
    print(moto_001)
    print(moto_002)
    print(moto_003)

if __name__ == '__main__':
    main()
