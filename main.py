#######################################################################
###########################   Bibliotecas   ###########################
#######################################################################

from random import random, randint
import math

#######################################################################
########################   Lectura de datos   #########################
#######################################################################

# Abierto como solo lectura : "r"
datos = open("datos1.txt", "r")

#######################################################################
######################   Variables generales   ########################
#######################################################################

# Cantidad maxima de ecuaciones aleatorias
maxEcuaciones = 10
# Valor Maximo Entero que hara de cociente
valMaxEnt = 10
# Cantidad de Factores que haran Q
canMaxFacQ = 3
# Cantidad de Factores que haran de potencia
canMaxFacPot = 2
# Lista donde se almacenan las Q
generacion = []
# determina si se genero un cociente
anteriorCociente = False


#######################################################################
##########################   Funciones   ##############################
#######################################################################

def generarnumrand():
    return random()


def generarnumrandint():
    return randint(2, valMaxEnt)


def polaridad(i):
    if i == 1:
        if generarnumrand() > 0.5:
            if generarnumrand() < 0.5:
                if i != 1:
                    return '+'
            else:
                return '-'
    return ''


def cociente():
    if generarnumrand() < 0.5:
        anteriorCociente = True
        return str(generarnumrandint()) + '*'
    return ''


def addTrigo_X_Y():
    n = generarnumrand()
    aux = ''

    if n < 0.2:
        aux += 'Sin('
        for j in range(1, canMaxFacPot + 1):
            aux += factorTrigo(j)
        aux += ')'
    elif n < 0.4:
        aux += 'Cos('
        for j in range(1, canMaxFacPot + 1):
            aux += factorTrigo(j)
        aux += ')'
    elif n < 0.6:
        aux += 'Tan('
        for j in range(1, canMaxFacPot + 1):
            aux += factorTrigo(j)
        aux += ')'
    elif n < 0.8:
        aux += '(X)'
    else:
        aux += '(Y)'

    return aux


def factorTrigo(j):
    aux = ''
    aux += polaridad(j)
    aux += cociente()
    aux += X_Y()
    aux += siguienteOperador(j, canMaxFacPot)

    return aux


def X_Y():
    if anteriorCociente:
        if generarnumrand() < 0.5:
            return '*(X)'
        else:
            return '*(Y)'
    else:
        if generarnumrand() < 0.5:
            return '(Y)'
        else:
            return '(X)'


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


def reemplazarX(ecuacion):
    aux = ''
    try:
        # Introducir valor de X
        aux = ecuacion.replace('X', '[X]')
    except:
        None

    return aux


def reemplazarY(ecuacion):
    aux = ''
    try:
        # Introducir valor de Y
        aux = ecuacion.replace('Y', '[Y]')
    except:
        None

    return aux


def reemplazarSin(ecuacion):
    aux = ''
    try:
        # Introducir valor de Y
        aux = ecuacion.replace('Sin', 'math.sin')
    except:
        None

    return aux


def reemplazarCos(ecuacion):
    aux = ''
    try:
        # Introducir valor de Y
        aux = ecuacion.replace('Cos', 'math.cos')
    except:
        None

    return aux


def reemplazarTan(ecuacion):
    aux = ''
    try:
        # Introducir valor de Y
        aux = ecuacion.replace('Tan', 'math.tan')
    except:
        None

    return aux


def corregirEcuacion(Q):
    cQ = reemplazarX(Q)
    cQ = reemplazarY(cQ)
    cQ = reemplazarSin(cQ)
    cQ = reemplazarCos(cQ)
    cQ = reemplazarTan(cQ)
    print('Ecuacion corregida:', cQ)
    # try:
    #    resultado = eval(Q)
    #    print('Evaluacion:', resultado)
    # except:
    #    print('Evaluacion: Error al evaluar')


#######################################################################
###   Generacion de ecuaciones aleatorias con canMaxFacQ Factores   ###
#######################################################################

for k in range(0, maxEcuaciones):
    # Ecuacion
    Q = ''

    # Generar factores
    for i in range(1, canMaxFacQ + 1):
        Q += '('
        # Polaridad
        Q += polaridad(i)

        # Cociente
        Q += cociente()

        # Funcion trigonometrica, X o Y
        Q += addTrigo_X_Y()

        Q += ')'

        # Siguiente operador
        Q += siguienteOperador(i, canMaxFacQ)

    print('\nEcuacion aleatoria:', Q)
    corregirEcuacion(Q)

datos.close()
