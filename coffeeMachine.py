import pandas as pd
import numpy as np

menu = {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "cost": 1.5,
    },

    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },

    "cappucino":{
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0
    }
}
menu = pd.DataFrame(menu)
resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
    'Money': 0,
}
resources = pd.Series(resources)

def processCoins(drink):
    total = 0
    cost = menu.loc['cost',drink]
    while total < cost:
        remaining = "{:.2f}".format(cost-total)
        coin = (input(f"Amount remaining £{remaining}. Please enter your coins or press C to cancel: "))
        if coin == "C":
                refund = "{:.2f}".format(total)
                print(f"Transaction cancelled. £{refund} refunded")
                return
        try:
            coin = round(float(coin), 2)
            total += coin
        except ValueError:
            print("Please enter a valid coin")
            continue
    resources['Money'] += cost
    return "{:.2f}".format(total-cost)

def checkResources(drink):
    check = (resources - menu[drink])
    is_enough = pd.Series([resource>=0 for resource in check.dropna()]).all()
    if is_enough:
                return True, check
    else:
        return False, list(check[check<=0].index)
    
def dispense(drink):
    check = checkResources(drink)
    if check[0] == True:       
        process = processCoins(drink)
        if process:
             print(f"*** Dispensing {drink} ***\nChange is £{process}")
             return check[1].fillna(resources).dropna()
        return
    else:
        print(f"Sorry there is not enough:",end=" ")
        print(*check[1],sep=", ")
        return resources

escape = False
while escape == False:
    drink = input("What would you like? (espresso/latte/cappucino): ")
    
    if drink in ["espresso","latte","cappucino"]:
        dispensed = dispense(drink)
        if dispensed is not None:
             resources = dispensed
             print(f"Here is your {drink}. Enjoy!\n")     
    
    elif drink == "report":
        money = "{:.2f}".format(resources.loc['Money'])
        print(f"Water: {resources.loc['water']}ml \nMilk: {resources.loc['milk']}ml \nCoffee: {resources.loc['coffee']}g \nMoney: £{money}")
        
    elif drink == "off":
        escape = True
    else:
        print("Please enter a valid input")


    


