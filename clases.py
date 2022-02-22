import random
import numpy as np

class Tablero:
	def __init__(self, columnas, filas):
		self.columnas = columnas
		self.filas = filas
		self.tabla_visiual = np.full((columnas,filas), fill_value = ' ')
		self.tabla_funcional = np.full((columnas,filas), fill_value = ' ')
	
	def print(self):
		print(self.tabla_visiual)
	
	def print_funcional(self):
		print(self.tabla_funcional)
	
	def es_acierto(self, columna, fila):
		if self.tabla_funcional[columna,fila] == "O":
			self.tabla_funcional[columna,fila] = 'X'
			self.tabla_visiual[columna,fila]= "X"
			return True

		elif self.tabla_funcional[columna,fila] == " ":
			self.tabla_funcional[columna,fila] = "*"
			self.tabla_visiual[columna,fila]= "*"

		elif self.tabla_funcional[columna,fila] == "X":
			pass

		elif self.tabla_funcional[columna,fila] == "*":
			pass

		return False
	
	def poner_barco(self, columna, fila, longitud, orientacion):
		if orientacion == 'H':
			self.tabla_funcional[fila,columna:columna+longitud] = 'O'
		elif orientacion == 'V':
			self.tabla_funcional[fila:fila+longitud,columna] = 'O'
		else:
			raise ValueError("El valor de orientación solo acepta \"ViH\"")

	#------------------------FALTA_POR_IMPLEMENTAR--------------------
	def es_posicion_legal(self, columna, fila, longitud, orientacion):
	#-----------------------------------------------------------------

		return True
	
	def generar(self, seed):
		if seed == 2:
			def subgenerar(cantidad, longitud):
				for i in range(cantidad):
					while True:
						columna = random.randint(0, self.columnas - 1)
						fila = random.randint(0, self.filas - 1)
						orientacion = 'H' if random.randint(0, 1) == 1 else 'V'
						
						if self.es_posicion_legal(fila, columna, longitud, orientacion):
							self.poner_barco(fila, columna, longitud, orientacion)
							break
			
			# Longitud 1
			subgenerar(4, 1)
			
			# Longitud 2
			subgenerar(3, 2)
			
			# Longitud 3
			subgenerar(2, 3)
			
			# Longitud 4
			subgenerar(1, 4)
		
		elif seed == 0:
			#---------------------_BARCOS_JUGADOR--------------------------------
			#Barcos_1:
			self.tabla_funcional[1,1:2] = 'O'
			self.tabla_funcional[5,3:4] = 'O'
			self.tabla_funcional[9,6:7] = 'O'
			self.tabla_funcional[7,1:2] = 'O'


			#Barcos_2
			self.tabla_funcional[1:3,3] = 'O'
			self.tabla_funcional[5,6:8] = 'O'
			self.tabla_funcional[8,7:9] = 'O'

			#Barcos_3
			self.tabla_funcional[6:9,4] = 'O'
			self.tabla_funcional[0,6:10] = 'O'

			#Barcos_4
			self.tabla_funcional[3,5:9] = 'O'
		
		elif seed == 1:
			#---------------------_BARCOS_CPU_---------------------------------
			#Barcos_1:
			self.tabla_funcional[4,5:6] = 'O'
			self.tabla_funcional[0,0:1] = 'O'
			self.tabla_funcional[8,8:9] = 'O'
			self.tabla_funcional[9,1:2] = 'O'


			#Barcos_2
			self.tabla_funcional[1:3,6] = 'O'
			self.tabla_funcional[5,7:9] = 'O'
			self.tabla_funcional[9,5:7] = 'O'

			#Barcos_3
			self.tabla_funcional[1:4,9] = 'O'
			self.tabla_funcional[4:7,2] = 'O'

			#Barcos_4
			self.tabla_funcional[2,1:5] = 'O'

class color:
    
    Verde = '\033[92m' #Verde
    Rojo = '\033[91m' #Rojo
    Azul = "\033[0;34m" #Azul
    Amarillo = "\033[1;33m" #Amarillo
    Reset = '\033[0m' 
