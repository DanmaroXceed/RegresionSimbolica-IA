#######################################################################
###########################   Bibliotecas   ###########################
#######################################################################

from random import random, randint

#######################################################################
########################   Lectura de datos   #########################
#######################################################################

# Abierto como solo lectura : "r"
datos = open("datos1.txt", "r")

#######################################################################
######################   Variables generales   ########################
#######################################################################

# Valor Maximo Entero que hara de cociente
valMaxEnt = 10
# Cantidad de Factores que haran Q
canMaxFacQ = 3
# Cantidad de Factores que haran de potencia
canMaxFacPot = 2
# Lista donde se almacenan las Q
generacion = []


#######################################################################
##########################   Funciones   ##############################
#######################################################################

def generarnumrand():
    return random()


def generarnumrandint():
    return randint(2, valMaxEnt)


def polaridad(i):
    if generarnumrand() > 0.5:
        if generarnumrand() < 0.5:
            if i != 1:
                return '+'
        else:
            return '-'
    return ''


def cociente():
    if generarnumrand() < 0.5:
        return str(generarnumrandint())
    return ''


def addTrigo_X_Y(X, Y):
    n = generarnumrand()
    aux = ''

    if n < 0.2:
        aux += 'Sin('
        for j in range(1, canMaxFacPot+1):
            aux += factorTrigo(j,X,Y)
        aux += ')'
    elif n < 0.4:
        aux += 'Cos('
        for j in range(1, canMaxFacPot+1):
            aux += factorTrigo(j,X,Y)
        aux += ')'
    elif n < 0.6:
        aux += 'Tan('
        for j in range(1, canMaxFacPot+1):
            aux += factorTrigo(j,X,Y)
        aux += ')'
    elif n < 0.8:
        aux += str(X)
    else:
        aux += str(Y)

    return aux


def factorTrigo(j,X,Y):
    aux = ''
    aux += polaridad(j)
    aux += cociente()
    aux += X_Y(X,Y)
    aux += siguienteOperador(j, canMaxFacPot)

    return aux

def X_Y(X,Y):
    if generarnumrand() > 0.5:
        return str(X)
    else:
        return str(Y)


def siguienteOperador(contador, limite):
    n = generarnumrand()
    aux = ''

    if contador != limite:
        if n < 0.25:
            aux += '*'
        elif n < 0.5:
            aux += '+'
        elif n < 0.75:
            aux += '/'
        else:
            aux += '-'

    return aux


#######################################################################
###   Generacion de ecuaciones aleatorias con canMaxFacQ Factores   ###
#######################################################################

for dato in datos:
    # Ecuacion
    Q = ''

    # print("x :", dato.split()[0],
    #      "\ny :", dato.split()[1],
    #      "\nR :", dato.split()[2], "\n")
    X = dato.split()[0]
    Y = dato.split()[1]
    R = dato.split()[2]

    # Generar factores
    for i in range(1, canMaxFacQ + 1):
        # Polaridad
        Q += polaridad(i)

        # Cociente
        Q += cociente()

        # Funcion trigonometrica, X o Y
        Q += addTrigo_X_Y(X, Y)

        # Siguiente operador
        Q += siguienteOperador(i, canMaxFacQ)

    print(Q)

datos.close()
