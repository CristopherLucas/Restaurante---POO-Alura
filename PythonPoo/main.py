from modelos.restaurante import Restaurante

tavola = Restaurante('Távola', 'Pizzaria')
tavola = Restaurante('Bar do Pedrão', 'Bar')
tavola.receber_avaliacao('Cris', 3)
tavola.receber_avaliacao('Lukas', 10)
tavola.receber_avaliacao('Tamiris', 10)


def main():
    Restaurante.listar_restaurante()


if __name__ == '__main__':
    main()
