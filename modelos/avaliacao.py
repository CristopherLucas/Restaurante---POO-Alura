
class Avaliacao():
    def __init__(self, cliente, nota):
        self.cliente = cliente
        self.nota = nota

    @classmethod
    def retornar_media(cls, lista_avaliacao):
        if not lista_avaliacao:
            return 'Sem Avaliações'
        return round(sum(avaliacao.nota for avaliacao in lista_avaliacao) / len(lista_avaliacao), 1)
