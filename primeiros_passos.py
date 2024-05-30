print("""
> Comandos/atalhos: 
      . ctrl+B (esconde/mostra a barra lateral); 
      . ctrl+J (abre/fecha a área de terminal) ;
      . ctrl+L (limpa o terminal, uma vez selecionado, semelhate ao 'clear');
      . ctrl+S (salva o arquivo, uma vez selecionado, antes de ser executado);
      . Escreva 'python nome_arquivo_executavel.py' no terminal (ctrl+J) p/ executar;
      . [...]
      """)

print('''
        >>> Esta é uma string que já fica formatada!
''')

print("""
    >>> Esta também é uma string que já fica formatada!!
""")

print('>> Função sep:','','A','N','D','R','É','', sep = '\n')
print('A','N','D','R','É', sep = '')
print('\n')
print('A','N','D','R','É', sep = ' ')
print('\n')

# Exemplo de comentário

# A linguagem Python utiliza o padrão snake_case, ou underscore_case

variavel_string_explicativa = 'f-string'

print(f'>> Esta é uma string chamada de {variavel_string_explicativa}, que permite interpolação de strings!!\n')

print(">> Aspas duplas também são aceitas!\n")

print('>> A interpolação ' + 'de strings pode' + ' ser feita com o operador + \n')

# Valor de pi arredondado
pi = 3.14159
## Abordagem f-string
print(f'> O valor arredondado de pi é: {pi:.2f}')
## Abordagem utilizando a função round()
print('> O valor arredondado de pi é:', round(pi,2))
## Abordagem .format()
print('> O valor arredondado de pi é: {:.2f} \n' .format(pi))


# Utilizando o input()
print('\n>> Declaração de variáveis\n')
variavel = input('> Digite um valor: ')
## O input() irá atribuir um valor do tipo string pra uma variável não inicializada com outro tipo
print(f'\n>> Tipo da variável {variavel}: {type(variavel)} \n')
print(f'>> Tipo do número 1, por exemplo: {type(1)}\n')
### A linguagem Python é fortemente tipada 
## Fazendo um Casting para o tipo int
variavel_nova = int(input('> Nova variável: '))
# ou então
variavel_nova = input('> Nova variável: ')
variavel_nova = int(variavel_nova)
print('\n')

# Estrutura if-elif-else 
idade = int(input('> Digite a sua idade: '))

if 0 < idade <= 12:
    print('>> Criança!!')
elif 12 < idade < 18:
    print('>> Adolescente!!')
elif idade >= 18:
    print('>> Adulto!!')
# Estrutura match (semelhante ao switch)
match idade:
    case 0:
        print('>> Recém-nascida!!')
    case 10:
        print('>> A criança tem 10 anos!!')
    case 28:
        print('>> O adulto tem 28 anos!!')

print()

# Criando lista

lista = []

for i in range(10):
    lista.append(i+1)
print('Lista:\n')
for item in lista:
    print(f'> {item}')

print()
