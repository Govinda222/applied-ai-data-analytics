print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
if size=="S":
    bill = 15
    print (f"You have selected Small size and the cost is $  {bill}")
elif size=="M":
    bill = 20
    print(f"you have selected Medium size and the cost is ${bill}")
elif size =="L":
    bill = 25
    print (f"You have selected Large pizza and the cost is ${bill}")
else :
    bill = 0
    print("No worries you can select in some other time ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
if pepperoni=="Y":
    if size == "S":
        extra_pepperoni = 2
        bill+=extra_pepperoni
        print ("Thanks for selecting the pepperoni")
    else:
        extra_pepperoni=3
        bill += extra_pepperoni
        print(f"Thanks for selecting the pepperoni")
else:
    print(f"No worries pizza still tastes good without pepperoni")
extra_cheese = input("Do you want extra cheese? Y or N: ")
if extra_cheese == "Y":
    cheese = 1
    bill+=cheese
    print(f"Thanks for selecting the cheese")
else :
    print("No worries pizza still taste good without cheese")
print("***********************************************************************************")
print(f"Your final bill is ${bill}")
