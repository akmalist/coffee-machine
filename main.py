# TODO: 1 print the report with all engredience once the user types report
# TODO: 2 ask the user a question ("What would you like? espresso/latte/ cappucino")
# TODO: 3 if the user answers the coffee type, ask the user if to insert coins and calculate
# TODO: 4 Calculate coins total vs coffee type total. If it is equal or higher substruct the total coins from the coffe cost and return the change to the customer
# TODO: 5 each time coffee has been made the report should substuct how much total left (Water, milk, coffee, etc)
# TODO: 6 Create a function that calculates coffee report
# TODO: 7 If there is not enought resources after calculating ( print "Sorry there is not enough item)


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
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


# calculate resourses
def safficient_transaction(item_ingrideients):
    for item in item_ingrideients:
        if item_ingrideients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


gameOn = True
profit = 0


# coins values
def calculate_coins():
    print("Please insert coins")
    quarters = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickles = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    total = quarters + dimes + nickles + pennies
    return total


def calculateCost(money, drink_cost):
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f'Here is your change {change}')
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingridients):
    """Deduct the required ingredients from the resources."""
    for item in drink_ingridients:
        resources[item] = resources[item] - drink_ingridients[item]
    print(f"Here is your {drink_name} ☕.Enjoy!")


while gameOn:
    askUser = input("What would you like? espresso/latte/cappuccino: ").lower()

    if askUser == "off":
        gameOn = False
    elif askUser == "report":
        print(f" Water :{resources['water']}ml")
        print(f" Milk :{resources['milk']}ml")
        print(f" Coffee :{resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[askUser]
        if safficient_transaction(drink['ingredients']):
            moneyReceived = calculate_coins()
            if (calculateCost(moneyReceived, drink['cost'])):
                make_coffee(askUser, drink['ingredients'])
