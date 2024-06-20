class Livro:

    livros = []

    def __init__(self, titulo='', autor='', ano_publicacao=0):
        self._titulo = titulo
        self._autor = autor
        self._ano_publicacao = ano_publicacao
        self._disponivel = True
        ## Adicionando livro na lista de livros
        Livro.livros.append(self)

    @property
    def titulo(self):
        return self._titulo
    
    @property
    def autor(self):
        return self._autor
    
    @property
    def ano_publicacao(self):
        return str(self._ano_publicacao)

    @property
    def disponivel(self):
        return 'disponivel' if self._disponivel else 'indisponivel'

    def __str__(self):
        return f'>> O livro \"{self.titulo}\", do(a) autor(a) {self.autor}, foi publicado em {self.ano_publicacao}! Está {self.disponivel}!'
    
    def emprestar(self):
        self._disponivel = False

    @classmethod
    def listar_livros(cls):
        print('\n>>> Listando todos os livros:\n')

        for book in cls.livros:
            print(f'\t> \"{book.titulo.ljust(5)}\", {book.autor.ljust(5)}, {book.ano_publicacao}. Estado: {book.disponivel}.')
        print()

    @staticmethod
    def verificar_disponibilidade(ano):
        livros_disponiveis = [book for book in Livro.livros if (book._ano_publicacao == ano and book._disponivel)]
        print(f'\n>>> Livros disponíveis de {ano}:\n')
        if not livros_disponiveis:
            print(f'\t> Não há livros disponíveis do ano {ano}!\n')
            return
        for book in livros_disponiveis:
            print(f'\t> \"{book.titulo.ljust(5)}\", {book.autor.ljust(5)}, {book.ano_publicacao}. Estado: {book.disponivel}.')
        print()


# Criando instâncias
livro_1 = Livro('It: a coisa', 'Stephen King', 1986)
livro_2 = Livro('É assim que acaba', 'Colleen Hoover', 2016)
livro_3 = Livro('O Iluminado', 'Stephen King', 1986)

# Imprimindo saídas
Livro.listar_livros()
print()

# Empréstimo(s)
livro_2.emprestar()
print(livro_2)
print()

# Verificando disponibilidade
Livro.verificar_disponibilidade(1986)