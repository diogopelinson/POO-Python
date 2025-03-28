from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('Praça', 'Brasileiro')
restaurante_planet_pizza = Restaurante('Planet Pizza', 'Pizza')
restaurante_mr_taxas = Restaurante('Mr Texas', 'Mexicano')

restaurante_mr_taxas.alternar_estado()
restaurante_planet_pizza.alternar_estado()
restaurante_praca.alternar_estado()

#Nota de 0 a 5
restaurante_praca.receber_avaliacao('Diogo', 6)
restaurante_praca.receber_avaliacao('Mariana', 2)
restaurante_praca.receber_avaliacao('Clovisvaldo', 3)

restaurante_mr_taxas.receber_avaliacao('João', 5)
restaurante_mr_taxas.receber_avaliacao('Roberto', 3)
restaurante_mr_taxas.receber_avaliacao('Adriana', 1)

restaurante_planet_pizza.receber_avaliacao('Jhonny', 1)
restaurante_planet_pizza.receber_avaliacao('Fernando', 4)
restaurante_planet_pizza.receber_avaliacao('Cleide', 3)


def main():
    Restaurante.listar_restaurantes()


if __name__ == '__main__':
    main()
