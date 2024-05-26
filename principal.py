# A partir del listado de equipos actualizado del Trabajo Práctico anterior, se
# generó el archivo de texto paises.csv que se entrega en este enunciado (haga
# click aquí o en el nombre del archivo para descargarlo). El significado de
# cada columna en el archivo es el siguiente:

    # confederación (es un valor de 0 a 5 que representa lo siguiente 0: UEFA, 1: CONMEBOL, 2: CONCACAF, 3: CAF, 4: AFC, 5: OFC)
    # nombre del pais
    # puntos de ranking de ese pais
    # cantidad de campeonatos ganados por ese pais

# A modo de ejemplo, entonces, la primera línea del archivo con los datos:
    # 4, Afganistán, 1052, 0 
# significa:
    # confederación: 4
    # nombre: Afganistán
    # puntos: 1052
    # cantidad de campeonatos ganados: 0

# A partir del archivo de texto paises.csv generar un vector de registros con
# el contenido del mismo. El vector debe generarse ordenado de manera
# descendente por puntos.

# Luego implementar un menú de opciones que permita:

# 1. Mostrar el listado completo de países, incluyendo el nombre de la
# confederación según su codificación numérica.

# 2. Informar cuál es el país con mayor cantidad de campeonatos ganados. Si
# fueran varios, informar todos.

# 3. Determinar, para cada confederación, cuántos países ganaron algún campeonato.

# 4. Generar un nuevo vector conteniendo los países de una confederación X que
# se ingresa por teclado. Los registros no deben incluir el campo confederación.
# Ordenar el vector por puntaje descendente y guardarlo en un archivo binario
# con nombre “clasificacionX.dat” donde X es el código de confederación.
# Mostrar un mensaje que indique nombre del archivo y cantidad de registros que
# contiene.

# 5. Ingresar una confederación por teclado y buscar su archivo de clasificación
# (realizado en el ítem anterior). Si no existe, generar su archivo de
# clasificación. Si existe, mostrar su contenido.

# 6. Preparar el fixture del próximo mundial: debe ser una matriz donde cada
# columna representa un grupo (8 grupos), cada fila el número de integrante de
# un grupo (4 integrantes por grupo) y la componente guarda el nombre de un país.
#
# a. En primer lugar, ingresar por teclado el nombre del país organizador
# (validarlo). Este será cabeza de serie del grupo A, ocupando la fila 0.

# b. Luego, definir los restantes “cabeza de serie”: son los siete países con
# mayor puntaje (excluyendo al organizador si estuviera entre ellos). Ubicarlos
# en la fila 0 de los grupos B a H.

# c. Por último, completar los grupos con 3 países más, por sorteo de manera
# aleatoria entre los 28 mejores restantes. Validar que no se repitan los
# países dentro de la matriz.

# d. Una vez generado mostrar el fixture por pantalla.

# 7. Buscar en el fixture realizado en el ítem anterior un país cuyo nombre se
# ingresa por teclado. Si existe, indicar qué grupo le corresponde. Si no
# existe, informarlo. (Verificar que el fixture ya se encuentre generado, en
# caso contrario, informar que no se puede procesar la solicitud).

# La gráfica que se muestra a continuación es UN EJEMPLO del contenido del
# fixture real para el último Mundial de Rusia 2018, pero quede claro: en
# este TP4 el fixture generado podrá ser OBVIAMENTE diferente, debido a que
# se pide confeccionar ese fixture combinando en forma aleatoria a los 31
# mejores equipos del archivo más el pais local.


import random
import os
from registro import *
from manejador_de_archivo import *
from validaciones import *


# PUNTO 1
def mostrar(vec):
    print('\n\t\t\t\t\t\t\t\t\t\t\tLISTADO DE PAÍSES')
    for paises in vec:
        to_string(paises)
    print('-' * 105)


# PUNTO 2
def punto_dos(paises):
    mayor = []
    for i in range(0, len(paises)):
        if len(mayor) == 0:
            mayor.append(paises[i])

        elif paises[i].campeonatos > mayor[0].campeonatos:
            mayor = [paises[i]]

        elif paises[i].campeonatos == mayor[0].campeonatos:
            mayor.append(paises[i])

    return mayor


# PUNTO 3
def contador_por_confederacion(paises):
    vec_acum = [0] * 6
    for pais in paises:
        if pais.campeonatos != 0:
            vec_acum[pais.confederacion] += 1
    return vec_acum


def mostar_camp_por_confederacion(v_confe):
    for i in range(len(v_confe)):
        print(CONFEDERACIONES[i], 'tiene un total de: ', v_confe[i], 'campeones.')


# PUNTO 4
def generar_vector_punto4(x, paises):
    v = []
    for pais in paises:
        if pais.confederacion == x:
            nomb = pais.nombre
            rank = pais.ranking
            camp = pais.campeonatos
            v.append(Paises_confederacion(nomb, rank, camp))
    return v


def ordenar_vector(vector_conf):
    n = len(vector_conf)
    for i in range(n - 1):
        for j in range(i+1, n):
            if vector_conf[i].ranking < vector_conf[j].ranking:
                vector_conf[i], vector_conf[j] = vector_conf[j], vector_conf[i]


def definir_resto_cabezas_de_series(matriz, paises):
    col = 7
    for i in range(col):
        if matriz[0][0] != paises[i].nombre:
            matriz[0][i+1] = paises[i].nombre

    for g in range(8):
        if matriz[0][g] is None:
            for m in range(8):
                if matriz[0][g] != paises[m].nombre:
                    matriz[0][g] = paises[m].nombre


def definir_resto_de_fixture(matriz, paises):
    col = 8
    fil = 4
    for c in range(col):
        for f in range(1, fil):
            esta = True
            while esta:
                num = random.randint(0, 36)
                pais = paises[num].nombre
                esta = validar_si_esta(matriz, pais)
                if not esta:
                    matriz[f][c] = pais


def mostrar_fixture(matriz):
    grupos = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    colum, fil = 8, 4
    print()
    print('\t\t\t\t \033[4;34mFIXTURE OFICIAL\033[0m')
    print()
    for c in range(colum):
        print('\033[32m-\033[0m' * 50)
        print('\033[31mGRUPO', grupos[c], '\033[0m')
        for f in range(fil):
            print(matriz[f][c])


# PUNTO 6
def generar_fixture(matriz, paises):
    pais_organizador = validar_pais_org(paises, 'Ingrese el nombre del país organizador: ')
    matriz[0][0] = pais_organizador
    definir_resto_cabezas_de_series(matriz, paises)
    definir_resto_de_fixture(matriz, paises)
    mostrar_fixture(matriz)


# PUNTO 7
def buscar_pais_punto7(matriz, arreglo):
    grupos = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H')
    x_pais = validar_pais_org(arreglo, 'Ingrese el nombre del país que desea buscar: ')
    for c in range(8):
        for f in range(4):
            if matriz[f][c] == x_pais:
                print()
                print('\033[34mBUSQUEDA EXITOSA')
                print(x_pais, 'pertenece al grupo: ', grupos[c], '\033[0m')
                return
    print()
    print('\033[34m', x_pais, 'no se encuentra en el fixture...\033[0m')


def principal():
    seis = False
    paises = generar_arreglo()
    op = -1
    while op != 0:
        print('\n\033[1;33mMUNDIAL RUSIA 2018\033[0;m\n')
        print(' 1. Mostrar listado completo de países')
        print(' 2. Mostrar países con más campeonatos ganados')
        print(' 3. Mostrar por confederacion, cuántos países ganaron algún campeonato')
        print(' 4. Generar un nuevo vector conteniendo los países de una confederación X')
        print(' 5. Buscar archivo de clasificación de una confederación')
        print(' 6. Mostrar fixture del próximo mundial')
        print(' 7. Buscar país en el fixture')
        print(' 0. SALIR ')
        op = validar_entre(0, 7, '\033[33m \n Ingrese número de la opción deseada: \033[0m')
        print()

        if op == 1:
            mostrar(paises)

        elif op == 2:
            if len(paises) != 0:
                mayor = punto_dos(paises)
                for linea in mayor:
                    to_string(linea)
                print('-' * 105)

        elif op == 3:
            if len(paises) != 0:
                v_confe = contador_por_confederacion(paises)
                mostar_camp_por_confederacion(v_confe)

        elif op == 4:
            if len(paises) != 0:
                x_conf = validar_entre(0, 5, 'Ingrese el número de confederación:'
                                             ' (0: UEFA, 1: CONMEBOL, 2: CONCACAF,'
                                             ' 3: CAF, 4: AFC, 5: OFC): ')
                vector_conf = generar_vector_punto4(x_conf, paises)
                ordenar_vector(vector_conf)
                fd = 'clasificacion' + str(x_conf) + '.dat'
                generar_archivo_binario(vector_conf, fd)
                print()
                print('\033[34m Se ha generado el archivo', fd, 'con una cantidad de',
                      len(vector_conf), 'registros \033[0m')

        elif op == 5:
            if len(paises) != 0:
                x_conf = validar_entre(0, 5, 'Ingrese el número de confederación:'
                                             ' (0: UEFA, 1: CONMEBOL, 2: CONCACAF,'
                                             ' 3: CAF, 4: AFC, 5: OFC): ')
                fd = 'clasificacion' + str(x_conf) + '.dat'
                buscar_archivo(fd, x_conf, paises)

        elif op == 6:
            if len(paises) != 0:
                seis = True
                matriz = [[None] * 8 for i in range(4)]
                generar_fixture(matriz, paises)

        elif op == 7:
            if len(paises) != 0 and seis:
                buscar_pais_punto7(matriz, paises)
            else:
                print('\033[31mNo se puede procesar la solicitud...')
                print('Genere primero el fixture presionando la opción "6" en '
                      'el menu de opciones. \033[0m')

        elif op == 0:
            print('\033[36m FIN DEL PROGRAMA \033[0m')
        print()


if __name__ == '__main__':
    principal()
