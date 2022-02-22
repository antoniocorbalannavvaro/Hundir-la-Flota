from funciones import *
from clases import color

print(color.Azul+"---------------------------------------------------------------------------------"+color.Reset)
print(color.Azul+"--------------------------------HUNDIR LA FLOTA----------------------------------"+color.Reset)
print(color.Azul+"---------------------------------------------------------------------------------\n"+color.Reset)

print(color.Amarillo+"REGLAS:"+color.Reset)
print("""\t1. El primero en hundir todos los barcos del rival GANA.
	2. Sólo se admiten coordenadas del 0 al 9.
	3. Debes elegir primero la coordenada 'X' y después la coordenada 'Y'.
	4. Si uno acierta a un barco vuelve a tirar.\n""")

while seguir_jugando():
	print_vidas()
	
	if not ha_acertado_cpu():
		disparar_jugador()

	if not ha_acertado_jugador():
		disparar_cpu()

if has_ganado():
	print("¡Has ganado!")

if has_perdido():
	print("¡Has perdido!")
