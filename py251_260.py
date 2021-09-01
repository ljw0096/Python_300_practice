class human:
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def who(self):
        print(f"이름:{self.name} 나이:{self.age} 성별:{self.sex}")
    def set_info(self,name,age,sex):
        self.name = name
        self.age = age
        self.sex = sex
areum = human("모름",0,"모름")
areum.set_info("아름",25,"여자")
areum.who()