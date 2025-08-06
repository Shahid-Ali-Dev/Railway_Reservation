print("Welcome to the Indian Railways")
f = input("Please Enter your name :")
print(f"Hello {f}, u can choose between Express and General seats by pressing 1 for the express or 2 for the general seat")
n = int(input("Enter your choice: "))
import random
express = 85
general = 221
pricing_express= 2000
pricing_general = 1000
class Train:
    # def __init__(self, express, general):
    #     self.express = express
    #     self.general = general
    
    if n == 1 and express != 0:
        print("You have chosen the express seat ")
        
        
        print(f"The price for the express seat is {pricing_express}")
        
        d = int(input("Are you traveling alone or with family\npress 1 for alone and 2 for family :"))
        if d == 1:
            e = 1
            print("You have chosen to travel alone")
            print(f"Your total cost is {pricing_express}")
        else:
            e = int(input("Enter the number of seats you want to book: "))
            print("You have chosen to travel with family")
            print(f"Your total cost is {pricing_express*e} for {e} members")

        c = input("Click \"ok\" to confirm your seat or \"no\" to cancel :")
        c.lower()
        if c == "ok":
            print(f"we have successfully reserved {e} seat or seats for {f}")
            print(f"Thank you for using our services {f}!")
            print(f"your seat number is {random.randint(1, express )}")
        else:
            print("The seat has been cancelled :")
    elif n == 1 and express == 0:
        print("Sorry the express trains are full at the moment, try for the next train!")
    
    elif n == 2 and general != 0:
        print("You have chosen the general seat")
        
       
        print(f"The price for the general seat is {pricing_general}")

        g = int(input("Are you traveling alone or with family\npress 1 for alone and 2 for family :"))
        if g == 1:
            h = 1
            print("You have chosen to travel alone")
            print(f"Your total cost is {pricing_general}")
        else:
            h = int(input("Enter the number of seats you want to book: "))
            print("You have chosen to travel with family")
            print(f"Your total cost is {pricing_general*h} for {h} members")

        i = input("Click \"ok\" to confirm your seat or \"no\" to cancel :")
        i.lower()
        if i == "ok":
            print(f"we have successfully reserved {h} seat or seats for {f}")
            print(f"Thank you for using our services {f}!")
            print(f"your seat number is {random.randint(1, general)}")
        else:
            print("The seat has been cancelled")
    elif n == 2 and general == 0:
        print("Sorry the general trains are full at the moment, try for the next train!")

    else:
        print("Invalid input")
    
    
Train()

       
