

class Electric_Co:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Tariff(Electric_Co):
    def __init__(self, name, location, t_name, pvt_price, com_price, Gen_type):
        self.t_name = t_name
        self.pvt_price = pvt_price
        self.com_price = com_price
        self.Gen_type = Gen_type
        super().__init__(name, location)

    def __str__(self):
        return ("Tariff Name = " + self.t_name + ", Price = [ "+ str(self.price)+ " ], " + "Generation Type = " + self.Gen_type)
