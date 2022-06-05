"""Las acciones que debe tener un jugador son:
1.- Tirada de dados
2.- Anotar recursos
3.- Comprar dado/carta
4.- Repetir acción en caso de que se quiera 
5.- Comprar dado/carta 
"""
import random
#Para los objetos de la tienda necesito saber el nombre del objeto, el valor de value, el price y la cantidad disponible

class Shop:
    def __init__ (self):
        self.items = {
            #Se realiza la definición de los materiales disponibles en la tienda.
            #debemos crear cada material e indicar el valor, el precio de la cara y la
            #cantidad que hay disponible para comprar.
            "gold": [
                {"value": 3,"price": 2, "stock": 4},
                {"value": 4,"price": 3, "stock": 4},
                {"value": 6,"price": 4, "stock": 1}
            ],
            "PV": [
                {"value": 3, "price": 8,"stock": 4},
                {"value": 4, "price": 12, "stock": 1}
            ],
            "sun": [
                {"value": 1, "price": 3, "stock": 4},
                {"value": 2, "price": 8, "stock": 4}
            ],
            "moon": [
                {"value": 1, "price": 2, "stock": 4},
                {"value": 2, "price": 6, "stock": 4}
            ],
            "combi":[
                {"value":{"PV":1, "sun":1}, "price":4, "stock": 1}
                
            ]
        }  

    def searchMat(self, material,val):
        thisMat=self.items[material]
        for idx, x in enumerate(thisMat):
            if thisMat[idx]["value"] == val:
                qty=idx
        return thisMat[qty]

    def checkingOnStock(self, material, val):
        #En la llamada de la función se tienen que indicar como argumentos de esta el material
        #y el valor de este, solamente se comprueba si hay o no stock del material deseado
        thisMat=self.searchMat(material,val)
        if thisMat["stock"]>0:
            return 1
        else:
            return 0

    def checkingPrice(self,material,val):
        #En esta función se comprueba el valor del material deseado
        thisMat=self.searchMat(material,val)
        return thisMat["price"]

    def buyDiceSide(self, material,val,money):    
        #Esta función es llamada a la hora de comprar un material y devuelve el precio de este
        #a la vez que descuenta una unidad en el stock del material
        if self.checkingOnStock(material,val) and self.checkingPrice(material,val)<money:
            self.searchMat(material,val)["stock"]-=1
            return self.checkingPrice(material,val)            
        else:
            print("no tienes la cantidad de gold suficiente para comprar la cara")


class Player:

    def __init__(self):
        self.inventory={
            "gold":10,
            "victoryPoints":0,
            "sun":0,
            "moon":0
        }
        self.matTyp=["gold", "luna", "sol", "PV"]
        self.sunDice=[]
        self.moonDice=[]

    def createDices(self):
        #Se crean ambos dados para todos los jugadores que tienen identica estructura   
        for x in range(0,6):
            self.sunDice.append([self.matTyp[0],1])
        self.sunDice[5]=[self.matTyp[2],1]
        self.moonDice=self.sunDice.copy()
        self.moonDice[4:6]=[[self.matTyp[1],1], [self.matTyp[3],2]]

    def throwDice(self, dice):
        return dice[random.randint(0,5)]

    def anotateResource(self, sunIdx):
        if self.sunDice[sunIdx][0]=="gold" and self.inventory["gold"]<12:
            self.inventory["gold"]+=self.sunDice[sunIdx][1]
        print(f"el gold que tiene el jugador es")

    def buyResources(self, material, val, replaceMat, replaceVal):
        """ 
        Para esta función se necesita obtener el oro del jugador, la lista de objetos de la tienda,
        comprobar que articulos tienen un precio por debajo del valor de oro que posee el jugador,
        Y que esta función llame a la función de cambiar value para poner la nueva value en lugar de otra
        """
        if self.inventory["gold"] >= shop.checkingPrice(material, val):
            for idx,x in enumerate(self.sunDice):
                if self.sunDice[idx][0]==replaceMat:
                    if self.sunDice[idx][1]==replaceVal:
                        self.sunDice[idx]=[material, val]
                break                    
        else:
            print("no hay oro suficiente para comprar esta cara")
            #habria que tener en cuenta el estado en el cual no tenga dinero para comprar  
            #nada o se arrepienta de su acción
    def chooseMat():
        print(2)




player1=Player()
shop=Shop()
player1.createDices()
player1.buyResources("gold",4,"gold",1)
print(player1.sunDice)

