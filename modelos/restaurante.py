from modelos.avaliacao import Avaliacao


class Restaurante:
    restaurantes = []  # type: ignore

    def __init__(self, nome, categoria):
        self.nome = nome.capitalize()
        self.categoria = categoria.capitalize()
        self._ativo = False
        self.avaliacoes = list()

        Restaurante.restaurantes.append(self)

    @classmethod
    def listar_restaurante(cls):
        print(f'{"Nome do restaurante".ljust(25)}|{"Categoria".ljust(25)}\
|{"Avaliação".ljust(25)}|Status\n')

        for restaurante in cls.restaurantes:
            print(
                f'{restaurante.nome.ljust(25)}|{restaurante.categoria.ljust(25)}\
|{str(Avaliacao.retornar_media(restaurante.avaliacoes)).ljust(25)}|{restaurante.ativo}')

    @property
    def ativo(self):
        return ('❌' if not self._ativo else '✔️')

    def alternar_estado(self):
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente, nota):
        if 0 < nota < 5:
            self.avaliacoes.append(Avaliacao(cliente, nota))
