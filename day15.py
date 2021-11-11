### Coffee Machine Code ###

"""
====================
OUTLINE
====================

What I need to happen:

Anytime you enter report it will print out a report of
the amount of coffee, water , milk, coins in the Machine

It processes coins, you put in a number of 50p coins or whatever.

Checks it has enough coffee.

Checks if it can do the transaction.

===========================
THE PLAN
===========================

what would you like?
 options:
    report

    cappuccino
    latte
    black

    after report need to print resources and coins
"""

Menu = {
        "cappuccino":   {
                "ingredients":  {
                        "water":250,
                        "milk":150,
                        "coffee":24
                                },
                "price":3.0
                        },
        "latte":        {
                "ingredients": {
                        "water":200,
                        "milk":150,
                        "coffee":24
                                },
                "price":2.5
                        },
        "espresso":     {
                "ingredients": {
                        "water":50,
                        "milk":0,
                        "coffee":18
                                },
                "price":1.5
                        }
        }

Resources = {
            "water":300,
            "milk":300,
            "coffee":300,
            "money":0
            }

def Report():
    print("Water :", Resources["water"])
    print("Milk :", Resources["milk"])
    print("Coffee :", Resources["coffee"])
    print("Money :", Resources["money"])


def Off():
    global On
    On = 0


def Order():
    order = "test"
    while order != "espresso" or "cappuccino" or "latte" or "report" or "off":
        print("What would you like? (Espresso/Latte/Cappuccino)")
        order = input()
        order = order.lower()
        print("test order", order)
    return order


def CheckResources(order):
    order = order.lower()
    for i in Resources:
        if Resources[i] - Menu[order]["ingredients"][i] < 0:
            return False
        else:
            return True


def MakeCoffee(order):
    order =  order.lower()
    for i in Resources:
        try:
            Resources[i] = Resources[i] - Menu[order]["ingredients"][i]
        except:
            pass
    print("Please take your", order)


def CoffeeMachine():
    while On == 1:
        order = Order()
        if order == "off":
            Off()
        elif order == "report":
            Report()
        else:
            if CheckResources(order) == True:
                MakeCoffee(order)
            else:
                print("Not enough resources")



On = 1
CoffeeMachine()

