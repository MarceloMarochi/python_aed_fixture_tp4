from registro import *
from principal import *
import os.path
import pickle


def add_in_order(vec, paises):
    n = len(vec)
    izq, der = 0, n-1
    pos = n
    while izq <= der:
        c = (izq + der) // 2

        if paises.ranking > vec[c].ranking:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq
        vec[pos:pos] = [paises]


def str_topaises(linea):
    token = linea.split(',')
    conf = int(token[0])
    nomb = token[1]
    rank = int(token[2])
    camp = int(token[3])
    paises = Paises(conf, nomb, rank, camp)
    return paises


def generar_arreglo():
    vec = []
    if os.path.exists('paises.csv'):
        m = open('paises.csv', 'rt', encoding='utf-8')
        for linea in m:
            paises = str_topaises(linea)
            add_in_order(vec, paises)
        m.close()

    return vec


def generar_archivo_binario(vec, fd):
    m = open(fd, 'wb')
    for linea in vec:
        pickle.dump(linea, m)
    m.close()


# PUNTO 5
def mostrar_archivo_punto5(fd):
    print('\033[34m \n\t\tArchivo ', fd, '\033[0m')
    print()
    m = open(fd, 'rb')
    t = os.path.getsize(fd)
    cad = '{:<30} | {:^10} | {:<10}'
    print(cad.format('Nombre', 'Ranking', 'Campeonatos'))
    while m.tell() < t:
        pais = pickle.load(m)
        print(to_string_punto4(pais))
    m.close()


def buscar_archivo(fd, x_conf, paises):
    if os.path.exists(fd):
        mostrar_archivo_punto5(fd)

    else:
        vector_conf = generar_vector_punto4(x_conf, paises)
        ordenar_vector(vector_conf)
        generar_archivo_binario(vector_conf, fd)
        print('\033[33m \nSe ha generado el archivo', fd, 'con una cantidad de ',
              len(vector_conf), 'registros \033[0m')
        mostrar_archivo_punto5(fd)
