from clases import Tablero

#--------------------_CONTEO_DE_VIDAS_------------------------
vidas_cpu = 21
vidas_jugador = 21

acierta_jugador = False
acierta_CPU = False

#-----------------_TABLEROS_---------------------------------

tablero_cpu = Tablero(10, 10)
tablero_jugador = Tablero(10, 10)

tablero_cpu.generar(1)
tablero_jugador.generar(0)

tablero_cpu.print_funcional()
