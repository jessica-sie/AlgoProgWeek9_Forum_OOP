class ShoppingJS:
    pass
    # initializer method 
    def __init__(self,food,amount):
        # item name
        self.__food = food
        # amount of items (pounds)
        self.__amount = amount
        # price per pound -> updated with private method
        self.__unitPrice = self.__unitPriceJS()
        # price of ordered item -> updated with public method
        self.__netPrice = self.netPriceJS()

    # private method stores: list of items, price per pound
    def __unitPriceJS(self):    
        if self.__food == "Dry Cured Iberian Ham":
            self.__unitPrice = 177.80
        elif self.__food == "Wagyu Steaks":
            self.__unitPrice = 450.00
        elif self.__food == "Matsutake Mushrooms":
            self.__unitPrice = 272.00
        elif self.__food == "Kopi Luwak Coffee":
            self.__unitPrice = 306.50
        elif self.__food == "Moose Cheese":
            self.__unitPrice = 487.20
        elif self.__food == "White Truffles":
            self.__unitPrice = 3600.00
        elif self.__food == "Blue Fin Tuna":
            self.__unitPrice = 3603.00
        elif self.__food == "Le Bonnotte Potatoes":
            self.__unitPrice = 270.81
        # trailing else that sets price to 0.00 if item is not on table
        else:  
            self.__unitPrice = 0.00

        return self.__unitPrice

    # public method to calculate the cost of the ordered food 
    def netPriceJS(self):
        # formula :amount of food in pounds x price per pound
        self.__netPrice = self.__amount * self.__unitPrice
        return self.__netPrice
        
    # accessor methods
    def getFood(self):
        return self.__food
    def getAmount(self):
        return self.__amount
    def getUnitPrice(self):
        return self.__unitPrice
    def getNetPrice(self):
        return self.__netPrice
    
        
