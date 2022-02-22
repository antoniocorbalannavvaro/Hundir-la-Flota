import numpy as np
import random
from variables import *
from clases import color

def disparar_cpu():

	global tablero_jugador

	global acierta_CPU
	global vidas_jugador

	columna =np.random.randint(0,10)
	fila =np.random.randint(0,10)
	print("La CPU ha disparado en las coordenadas",columna,fila)

	if tablero_jugador.es_acierto(columna,fila):
		vidas_jugador -= 1
		acierta_CPU = True
		print("Ha acertado")

	else:
		acierta_CPU = False
		print("Ha fallado")


	print(color.Amarillo+"Te quedan",vidas_jugador,"vidas."+color.Reset)
	print(color.Amarillo+"A la CPU le quedan",vidas_cpu,"vidas."+color.Reset)
	tablero_jugador.print()


def disparar_jugador():

	global tablero_cpu

	global acierta_jugador
	global vidas_cpu

	while True:

		try:

			columna = int(input("¿En qué coordenadas X quieres disparar?: "))
			fila = int(input("¿En qué coordenadas Y quieres disparar?: "))

			if not 0 <= columna <= 9 or not 0 <= fila <= 9:
			#if columna < 0 or columna > 9 or fila < 0 or fila > 9:
				raise ValueError('Valore fuera de rango')

			break

		except ValueError:
			print("Sólo se admiten valores entre el 0 y 9.")
			


	print("Has disparado en las coordenadas",columna,fila)


	if tablero_cpu.es_acierto(columna,fila):
		vidas_cpu -= 1
		acierta_jugador = True
		print("Has acertado")

	else:
		acierta_jugador = False
		print("Has fallado")


	print(color.Amarillo+"Te quedan",vidas_jugador,"vidas."+color.Reset)
	print(color.Amarillo+"A la CPU le quedan",vidas_cpu,"vidas."+color.Reset)
	tablero_cpu.print()


def print_vidas():
	print(color.Verde+"VIDAS JUGADOR: "+str(vidas_jugador)+color.Reset+"\t"+color.Rojo+"VIDAS CPU: "+str(vidas_cpu)+color.Reset+"\n")

def seguir_jugando():
	return vidas_cpu > 0 and vidas_jugador > 0

def has_ganado():
	return vidas_cpu == 0

def has_perdido():
	return vidas_jugador == 0

def ha_acertado_cpu():
	return acierta_CPU

def ha_acertado_jugador():
	return acierta_jugador


