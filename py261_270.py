class Stock:
    def __init__(self,name,code,PER,PBR,profit):
        self.name = name
        self.code = code
        self.PER = PER
        self.PBR = PBR
        self.profit = profit
    def set_name(self,name):
        self.name = name
    def set_code(self,code):
        self.code = code
    def set_PER(self, PER):
        self.PER = PER
    def set_PBR(self,PBR):
        self.PBR = PBR
    def set_profit(self,profit):
        self.profit = profit
    def get_name(self):
        return self.name
    def get_code(self):
        return self.code
    def get_PER(self):
        return self.PER
    def get_PBR(self):
        return self.PBR
    def get_profit(self):
        return self.profit
    
    
samsung = Stock("삼성전자","005930",15.79,1.33,2.83)
hyundai = Stock("현대차","005380",8.70,0.35,4.27)
LG = Stock("LG전자","066570",317.34,0.69,1.37)

stock_list = [samsung,hyundai,LG]

for val in stock_list:
    print(val.get_code())
    print(val.get_PER())