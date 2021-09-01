import random

class Account:
    account_count = 0

    def __init__(self, client, money):

        self.bank = "SC은행"
        self.client = client
        self.money = money
        
        num1 = random.randint(0,999)
        num2 = random.randint(0,99)
        num3 = random.randint(0,999999)

        num1 = str(num1).zfill(3)
        num2 = str(num2).zfill(2)
        num3 = str(num3).zfill(6)
        self.account_number = num1+'-'+num2+'-'+num3

        Account.account_count += 1
        self.deposit_time = 0
        self.deposit_list=[]
        self.withdraw_list=[]
    @classmethod
    def get_account_num(cls):
        return cls.account_count

    def deposit(self,cash):
        if cash<1:
           return
        else:
           self.money += cash
           self.deposit_time += 1
           self.deposit_list.append(cash)
           if self.deposit_time % 5 == 0:
                self.money += self.money*0.01
            

        
    def withdraw(self, cash):
        if cash>self.money:
            return
        else:
            self.money -= cash
            self.withdraw_list.append(-cash)
            
    def display_info(self):
        print("은행이름 : "+self.bank)
        print("예금주 : "+self.client)
        print("계좌번호" + self.account_number)
        print("잔고 : "+str(self.money))

    def deposit_history(self):
        print(self.deposit_list)
    def withdraw_history(self):
        print(self.withdraw_list)
kim = Account("김민수",100)

lee = Account("이지원",100)

park = Account("박박박",10000000)

client_list = [kim,lee,park]

park.deposit(100)
park.deposit(100)
park.deposit(100)
park.deposit(100)

park.withdraw(10)
park.withdraw(10)
park.withdraw(10)

park.deposit_history()
park.withdraw_history()