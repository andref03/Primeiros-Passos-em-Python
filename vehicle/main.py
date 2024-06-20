from carro import Carro
from moto import Moto

# Criando instâncias
## Carros
carro_001 = Carro('Fiat', 'Kwid', 4, 'Vermelho')
carro_003 = Carro('Renault', 'Sandero', 4, 'Cinza')
carro_002 = Carro('Honda', 'Civic', 2, 'Preto')
## Motos
moto_001 = Moto('Yamaha', 'MT-09', 'Esportiva')
moto_002 = Moto('Honda', 'CB 500', 'Casual')
moto_003 = Moto('Harley-Davidson', 'Street 750', 'Esportiva')

# Ligando veículos
carro_003.ligar()
moto_002.ligar()
moto_003.ligar()

def main():
    print(carro_001)
    print(carro_002)
    print(carro_003)
    print(moto_001)
    print(moto_002)
    print(moto_003)

if __name__ == '__main__':
    main()
