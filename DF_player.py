import random
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

    def throwDice(self):
        throw1=random.randint(0,5)
        throw2=random.randint(0,5)
        return (self.moonDice[throw1], self.sunDice[throw2])


    def anotateResource(self, sunIdx):
        if self.sunDice[sunIdx][0]=="gold" and self.inventory["gold"]<12:
            self.inventory["gold"]+=self.sunDice[sunIdx][1]
        print(f"el gold que tiene el jugador es")

    def buyResources(self, material, val, replaceMat, replaceVal, shop):
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
    def chooseMat(self, shop):
        selection=""
        for idx,x in enumerate(shop.items["combi"]):
            if shop.items["combi"][idx]["value"] == {"PV":1, "sun":1} :
                for idx, key in enumerate(shop.items["combi"][idx]["value"]):
                    selection=str(idx)+":"+key+" "+selection
                print(selection)
                chosenMat=input("elige que recurso te interesa: ")
                print(chosenMat)