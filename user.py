

class Bill(object):
    def __init__(self, userid, monthly_Consumption, month):
        self.userid = userid
        self.monthly_Consumption = monthly_Consumption
        self.month = month

class User(Bill):
    def __init__(self, userid, name, occupants, C_Type, location, G_type, monthly_Consumption, month):
        self.userid = userid
        self.name = name
        self.occupants = occupants
        self.C_Type = C_Type
        self.location = location
        self.G_type = G_type
        super().__init__(userid, monthly_Consumption, month)
