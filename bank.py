class ContaBancaria:
    def __init__(self, titular='', saldo=0):
        self._titular = titular
        self._saldo = saldo
        self._ativo = False
    
    @property
    def titular(self):
        return self._titular
    
    @property
    def saldo(self):
        return self._saldo

    @property
    def ativo(self):
        return 'ativo' if self._ativo else 'inativo'

    def __str__(self):
        return f'>> Olá, {self.titular}! O seu saldo bancário atual é  R$ {self.saldo}, e o estado da sua conta está {self.ativo}'

    @classmethod
    def ativar_conta(cls, titular):
        titular._ativo = True 

    
titular_1 = ContaBancaria('André Felipe', 3500)
titular_2 = ContaBancaria('Joaquim José', 2850)

print(titular_1)
print(titular_2)
print()

ContaBancaria.ativar_conta(titular_1)
ContaBancaria.ativar_conta(titular_2)

print(titular_1)
print(titular_2)
print()

print(f'>> Titular da primeira conta: {titular_1.titular}')
