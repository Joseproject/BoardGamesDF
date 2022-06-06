"""Las acciones que debe tener un jugador son:
1.- Tirada de dados
2.- Anotar recursos
3.- Comprar dado/carta
4.- Repetir acción en caso de que se quiera 
5.- Comprar dado/carta 
"""
import random
#Para los objetos de la tienda necesito saber el nombre del objeto, el valor de value, el price y la cantidad disponible
player1=Player()
shop=Shop()
player1.createDices()
player1.buyResources("gold",4,"gold",1)
print(player1.sunDice)