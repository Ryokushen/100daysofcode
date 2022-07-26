from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeemenu = Menu()
coffeemaker = CoffeeMaker()
moneymachine = MoneyMachine()


def process_transaction():
    order_name = input("What would you like? Latte, Cappuccino, or Espresso? \n").lower()

    if order_name == 'report':
        coffeemaker.report()
        moneymachine.report()
        process_transaction()
    elif order_name == 'off':
        exit()

    drink = coffeemenu.find_drink(order_name)

    if drink is None:
        exit()

    if not coffeemaker.is_resource_sufficient(drink):
        exit()

    if moneymachine.make_payment(drink.cost):
        coffeemaker.make_coffee(drink)
        process_transaction()
    else:
        process_transaction()


process_transaction()

