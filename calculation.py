from tariff import Tariff
from user import User
from comparator import Comparator


# Object For Electric Companies ( Name ,
Elect_Com = []
Elect_Com.append(Tariff("ENTEGA",['Freiburg','Stuttgart','Karlsruhe','Frankfurt','Berlin','Munich'] , "GrunerTraum", 7.12 , 9.12, "Green" ))
Elect_Com.append(Tariff("Eon",['Freiburg','Stuttgart','Karlsruhe','Frankfurt','Berlin','Munich'] , "Grun_Energien", 7.45 , 9.45, "Green" ))
Elect_Com.append(Tariff("Badenova",['Freiburg','Stuttgart','Karlsruhe','Frankfurt'], "Express_Package", 6.25, 8.25, "Mixed"))
Elect_Com.append(Tariff("EnBW",['Freiburg','Stuttgart','Karlsruhe','Frankfurt'], "EnBW_Package", 6.95, 8.95, "Mixed"))


## Object For Consumers ( USERId, Name , Occupants , Type of Consumer , Location , Generation Type Needed , Monthly Consumption , Month )
User_Profile = []
User_Profile.append(User("123", "Jack", 3, "Pvt", "Freiburg", "Green", 300, 1))
User_Profile.append(User("125", "Jone", 100, "Com", "Freiburg", "Mixed", 1500, 1))
User_Profile.append(User("127", "Tom", 5, "Pvt", "Stuttgart", "Mixed", 450, 1))
User_Profile.append(User("129", "Julia", 1, "Pvt", "Karlsruhe", "ANY", 200, 1))

# Calculate Prices for Single Consumer based on its choice

best=[]
for x in range((len(Elect_Com))):
    best.append(Comparator.price_comparator_text(Elect_Com[x], User_Profile[2]))

# print("End")
