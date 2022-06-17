"""Las acciones que debe tener un jugador son:
1.- Tirada de dados
2.- Anotar recursos
3.- Comprar dado/carta
4.- Repetir acción en caso de que se quiera 
5.- Comprar dado/carta 
"""
from asyncio.windows_events import NULL
import random
from re import A
import DF_player
import DF_shop
import DF_gameBoard
#player1, player2, player3, player4=""
player=[1,2,3,4]
#Para los objetos de la tienda necesito saber el nombre del objeto, el valor de value, el price y la cantidad disponible
#player=[player1, player2, player3, player4]
for x in range(4):
    print(x)
    player[x]=DF_player.Player()
shop=DF_shop.Shop()
player[0].createDices()
player[0].buyResources("gold",4,"gold",1, shop)
print(player[0].sunDice)
print(player[0].moonDice)
#player[].chooseMat(shop)
player[0].anotateResource()
DF_gameBoard.gameBoard.playerMovement("portal1", player[0], 4)
print(player[0].ubi)