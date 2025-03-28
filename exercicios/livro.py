class Livro:
    def __init__(self, titulo, autor, ano_publicaco):
        self._titulo = titulo.title()
        self._autor = autor
        self._ano_publicacao = ano_publicaco
        self._disponivel = True
      

    def __str__(self):
        return f'{self._titulo} | {self._autor} | {self._ano_publicacao} '


livro1 = Livro('As 48 leis do poder', 'Robert Greene', 1998)
livro2 = Livro('Hábitos Atômicos', 'James Clear', 2018)

print(livro1)
print(livro2)



def emprestar(self):
    self.disponivel = False


livro3 = Livro('A vaca roxa', 'Seth Godin', 2018)
print(f"Antes de emprestar: Livro disponível? {livro3.disponivel}")
livro3.emprestar()
print(f"Depois de emprestar: Livro disponível? {livro3.disponivel}")


def verificar_disponibilidade(ano):
    livros_disponiveis = [livro for livro in Livro.livros if livro.ano_publicacao == ano and livro.disponivel]
    return livros_disponiveis

Livro.livros = [livro1, livro2, livro3]
