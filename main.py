MENU = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    print(f"Water: {resources['water']}")
    print(f"Milk: {resources['milk']}")
    print(f"Coffee: {resources['coffee']}")
    print(f"Money:${resources['money']}")


shortage = True
resources['money'] = 0.00


def coffee_machine():
    drink_choice = input("What would you like? Latte, Cappuccino, or Espresso? \n").title()

    if drink_choice == 'Report':
        report()
        coffee_machine()
    elif drink_choice == 'Off':
        exit()

    if drink_choice == 'Espresso':
        drink_cost = MENU[drink_choice]['cost']
        drink_water = MENU[drink_choice]['ingredients']['water']
        drink_coffee = MENU[drink_choice]['ingredients']['coffee']
    else:

        drink_cost = MENU[drink_choice]['cost']
        drink_water = MENU[drink_choice]['ingredients']['water']
        drink_milk = MENU[drink_choice]['ingredients']['milk']
        drink_coffee = MENU[drink_choice]['ingredients']['coffee']

    def drinkresource(drink):
        if drink == 'Espresso':
            drink_waters = MENU[drink]['ingredients']['water']
            drink_coffees = MENU[drink]['ingredients']['coffee']
            if drink_waters > resources['water']:
                print("Sorry there is not enough water.")
                shortage1 = True
                return shortage1
            if drink_coffees > resources['coffee']:
                print("Sorry there is not enough coffee.")
                shortage1 = True
                return shortage1
        else:
            drink_waters = MENU[drink]['ingredients']['water']
            drink_milks = MENU[drink]['ingredients']['milk']
            drink_coffees = MENU[drink]['ingredients']['coffee']
            if drink_waters > resources['water']:
                print("Sorry there is not enough water.")
                shortage1 = True
                return shortage1
            if drink_milks > resources['milk']:
                print("Sorry there is not enough milk.")
                shortage1 = True
                return shortage1
            if drink_coffees > resources['coffee']:
                print("Sorry there is not enough coffee.")
                shortage1 = True
                return shortage1

    is_shortage = drinkresource(drink_choice)
    if is_shortage == shortage:
        exit()
    else:
        if drink_choice == 'Espresso':
            resources['water'] = resources['water'] - drink_water
            resources['coffee'] = resources['coffee'] - drink_coffee
            resources['money'] = resources['money'] + drink_cost
        else:
            resources['water'] = resources['water'] - drink_water
            resources['milk'] = resources['milk'] - drink_milk
            resources['coffee'] = resources['coffee'] - drink_coffee
            resources['money'] = resources['money'] + drink_cost

    def payment(q, d, n, p):
        quart = q * 0.25
        dime = d * 0.10
        nick = n * 0.05
        pen = p * 0.01
        total = quart + dime + nick + pen
        return total

    print("Please insert coins.")

    quarters = int(input("How many quarters?"))
    dimes = int(input("How many dimes?"))
    nickels = int(input("How many nickels?"))
    pennies = int(input("How many pennies?"))

    customer_pay = payment(q=quarters, d=dimes, n=nickels, p=pennies)

    if customer_pay > drink_cost:
        change = round(customer_pay - drink_cost, 2)
        print(f"Here is ${change} in change.")
        print(f"Here is your {drink_choice} ☕. Enjoy!")
        coffee_machine()
    else:
        print("Sorry That's not enough money. Money refunded.")
        coffee_machine()


coffee_machine()


