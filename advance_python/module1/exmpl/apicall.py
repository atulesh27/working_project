def apicall():
    print("Api call function from api module")

class emp:
    def __init__(self,name,age,sal):
        self.name = name
        self.age = age
        self.sal =  sal


    def show(self):
        print(f" i am {self.name} , my age is {self.age} with salary in hand - {self.sal} ")