CONFEDERACIONES = ['UEFA', 'CONMEBOL', 'CONCACAF', 'CAF', 'AFC', 'OFC']


class Paises:
    def __init__(self, conf, nomb, rank, camp):
        self.confederacion = conf
        self.nombre = nomb
        self.ranking = rank
        self.campeonatos = camp


class Paises_confederacion:
    def __init__(self, nomb, rank, camp):
        self.nombre = nomb
        self.ranking = rank
        self.campeonatos = camp


def to_string_punto4(paises):
    cad = '{:<30} | {:^10} | {:<10}'
    return cad.format(paises.nombre, paises.ranking, paises.campeonatos)


def to_string(paises):
    r = ""
    r += "{:<30}".format("Confederación: " + (CONFEDERACIONES[paises.confederacion]))
    r += "{:<40}".format("Nombre: " + str(paises.nombre))
    r += "{:<20}".format("Ranking: " + str(paises.ranking))
    r += "{:<15}".format("Campeonatos: " + str(paises.campeonatos))
    print('-' * 105)
    print(r)
