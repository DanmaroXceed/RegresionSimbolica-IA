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
canMaxFacQ = 10
# Cantidad de Factores que haran de potencia
canMaxFacPot = 10
# Lista donde se almacenan las Q
generacion = []

#######################################################################
###   Generacion de ecuaciones aleatorias con canMaxFacQ Factores   ###
#######################################################################

for dato in datos:
    # Ecuacion
    Q = ''

    print("x :", dato.split()[0],
          "\ny :", dato.split()[1],
          "\nR :", dato.split()[2], "\n")

    # print()

datos.close()
