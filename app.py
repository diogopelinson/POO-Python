from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

restaurante_praca = Restaurante('Praça', 'Brasileiro')
bebida_suco = Bebida('Suco de Uva', 5.0, 'Grande')
prato_feijoada = Prato('Feijoada', 25.0, 'Melhor feijuca da cidade!')
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(prato_feijoada)

def main():
   restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
