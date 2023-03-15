addOns = {
    "Cheese": 100,
    "MozzarellaCheese": 150,
    "Pepper": 80,
    "BaconHam": 120,
    "Mushroom": 130,
    "OnionsChili": 110,
    "Tomato": 90,
    "Pineapple": 100,
    "Salami": 120
}


def calculateCost(addOnsList):
    cost = 450
    for addOn in addOnsList:
        cost += addOns[addOn]
    return cost


def Deluxe():
    addOnsList = ["Cheese", "BaconHam", "OnionsChili"]
    cost = calculateCost(addOnsList)
    return addOnsList, cost


def Special():
    addOnsList = ["Cheese", "Pepper", "BaconHam", "Mushroom", "OnionsChili"]
    cost = calculateCost(addOnsList)
    return addOnsList, cost


def Primo():
    addOnsList = ["MozzarellaCheese", "Pepper", "BaconHam", "Mushroom", "OnionsChili", "Tomato", "Pineapple", "Salami"]
    cost = calculateCost(addOnsList)
    return addOnsList, cost


customerName = input("Enter customer name: ")
print("Hello", customerName + "! Welcome to Pizza Kiosk.\n")

print("Choose your pizza:")
print("1. Deluxe")
print("2. Special")
print("3. Primo")
choice = int(input("Enter your choice (1-3): "))

if choice == 1:
    addOnsList, cost = Deluxe()
elif choice == 2:
    addOnsList, cost = Special()
elif choice == 3:
    addOnsList, cost = Primo()
else:
    print("Invalid choice. Please try again.")
    exit()

FinalPizzaChoice = {
    "customerName": customerName,
    "pizzaType": choice,
    "addOns": addOnsList,
    "cost": cost
}

print("\nYour pizza details:")
print("Pizza type:", choice)
print("Add-ons:", addOnsList)
print("Cost:", cost)

print("\nPlease pay", cost, "at the counter. Thank you for visiting Pizza Kiosk!")