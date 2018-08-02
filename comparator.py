
class Comparator:
    def price_comparator_text(tariffa, usera):
        if tariffa.Gen_type == usera.G_type or usera.G_type == 'ANY':
            if usera.C_Type == 'Pvt':
                T_p = (tariffa.pvt_price/100) * usera.monthly_Consumption
            else:
                T_p = (tariffa.com_price/100) * usera.monthly_Consumption
            print("Company Name: " + tariffa.name + " , Tariff: " + tariffa.t_name + " , Price: " + str(T_p) + " Euros/Month");

            return T_p, tariffa.t_name, tariffa.name
        else:
            #print ("Parameters Doesn't Match")
            T_p=None
            return T_p, tariffa.t_name, tariffa.name


