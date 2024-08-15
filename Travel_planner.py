class Travel:
    def __init__(self,country,month,type):
        self.country=country
        self.month=int(month)
        self.type=type
        self.price=0
    def details(self):
        if self.month>=3 and self.month<=10:
            print(f"you goin to {self.country} in summer and the trip is {self.type}")
        elif self.month<3 and self.month>10:
            print(f"you are going to {self.country} in winter and the trip is {self.type}")
        else:
            print("invalid input")
    def cal_cost(self,cost):
        costs=[]
        while cost != 0:
            self.price += cost
            costs.append(cost)
            cost = int(input("Enter another cost: "))
        advice = self.advice(self.price)
        check=self.check_cost(costs)
        return advice,check

    def advice(self,num):
        if num<=500:
            print("low budget")
        elif num>500 and num<=1500:
            print("you can travel any where")
        else:
            print("luxury trip")
    def check_cost(self,costs):
        cost_check=0
        for i in costs:
            if i>=10:
                cost_check+=1
        if cost_check<=10:
            self.price+=100
            print(f"the updated price is: {self.price}")

country=input("Enter country: ")
month=input("Enter the month: ")
travetype=input("Business or leisure: ")

mytrave=Travel(country,month,travetype)
mytrave.details()
mycost=int(input("ENter flight cost: "))
mytrave.cal_cost(mycost)


