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
