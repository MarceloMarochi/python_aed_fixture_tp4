from registro import *
from principal import *


def validar_entre(x, y, mensaje):
    num = int(input(mensaje))
    print()
    while num < x or num > y:
        num = int(input('\033[31mINCORRECTO\033[0m, por favor ' + mensaje))
    return num


def validar_pais_org(paises, mensaje):
    flag = False
    pais = input(mensaje)
    while not flag:
        for linea in paises:
            if pais == linea.nombre:
                return pais
        else:
            print()
            print('\033[31mEl nombre ingresado no corresponde a ningún país...')
            print('Por favor escriba respetando las siguientes indicaciones: ')
            print('Primera letra en mayúscula y el resto en minúscula, ejemplo: "Argentina"\033[0m')
            print()
            pais = input('Por favor, ' + mensaje)


def validar_si_esta(matriz, x):
    for c in range(8):
        for f in range(4):
            if matriz[f][c] == x:
                return True
    return False
