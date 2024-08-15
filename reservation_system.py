class Guest:
    def __init__(self,first,last,rank,age):
        self.first=first
        self.last=last
        self.rank=int(rank)
        self.age=int(age)
    def guest_info(self,all_guest):
        for guest in all_guest:
            print(f"{guest.first} {guest.last} age: {guest.age}")
    def loyal_program(self,all_guest):
        Gold_members=[guest.last for guest in all_guest if guest.rank>=10]
        if Gold_members:
            print("Gold Members: ")
        for member in Gold_members:
            print("\t Guest:",member)
    def guest_avg(self,all_guest):
        total_age=0
        for guest in all_guest:
            total_age+=guest.age
        avg_age=total_age/len(all_guest)
        print("The average of guests is: ",avg_age)
all_guest=[]
number_of_guest=int(input("Enter number of guests: "))
for i in range(number_of_guest):
    guest_data=input("Input guest data as: firstname/lastname/rank/age: ").split("/")
    guest=Guest(guest_data[0],guest_data[1],guest_data[2],guest_data[3])
    all_guest.append(guest)
guest=all_guest[0]
guest.guest_info(all_guest)
guest.loyal_program(all_guest)
guest.guest_avg(all_guest)