# print("Starting to make a coffee")
# print("Grinding coffee beans")
# print("Boiling water")
# print("Mixing boiled water with crushed coffee beans")
# print("Pouring coffee into the cup")
# print("Pouring some milk into the cup")
# print("Coffee is ready!")


# print("For "+ num +" cups of coffee you will need:")

# water = int(num) * 200
# milk = int(num) * 50
# coffee = int(num) * 15

# print(str(water)+" ml of water")
# print(str(milk)+" ml of milk")
# print(str(coffee)+ " g of coffee beans")
# rem_water = water_cap - water
# rem_milk = milk_cap - milk
# rem_coffee = coffee_cap - coffee
# print("how many ml of water the coffee machine has:")


# print("how many ml of milk the coffee machine has:")


# print("how many grams of water the coffee machine has:")


# p = water_cap // 200
# q = milk_cap // 50
# r = coffee_cap // 15

# cup_pos = min(p,q,r)
# Write your code here
water_cap = 400
milk_cap = 540
coffee_cap = 120
disposable_cups = 9
money_have = 550


def buy_action():
    coffee_type = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    global water_cap
    global coffee_cap
    global money_have
    global milk_cap
    global disposable_cups

    if coffee_type == "1":
        if water_cap > 250 and coffee_cap > 16:
            print("I have enough resources, making you a coffee!")
            water_cap = water_cap - 250
            coffee_cap = coffee_cap - 16
            money_have = money_have + 4
            disposable_cups = disposable_cups - 1
        else:
            if water_cap < 250:
                print("Sorry, not enough water!")
            if coffee_cap < 16:
                print("Sorry, not enough coffee!")
    elif coffee_type == "2":
        if water_cap > 350 and milk_cap > 75 and coffee_cap > 20:
            print("I have enough resources, making you a coffee!")
            water_cap = water_cap - 350
            milk_cap = milk_cap - 75
            coffee_cap = coffee_cap - 20
            money_have = money_have + 7
            disposable_cups = disposable_cups - 1
        else:
            if water_cap < 350:
                print("Sorry, not enough water!")
            if coffee_cap < 16:
                print("Sorry, not enough coffee!")
            if milk_cap < 75:
                print("Sorry, not enough milk!")
    elif coffee_type == "3":
        if water_cap > 200 and milk_cap > 100 and coffee_cap > 12:
            print("I have enough resources, making you a coffee!")
            water_cap = water_cap - 200
            milk_cap = milk_cap - 100
            coffee_cap = coffee_cap - 12
            money_have = money_have + 6
            disposable_cups = disposable_cups - 1
        else:
            if water_cap < 200:
                print("Sorry, not enough water!")
            if coffee_cap < 12:
                print("Sorry, not enough coffee!")
            if milk_cap < 100:
                print("Sorry, not enough milk!")
    else:
        return


def take_action():
    global money_have
    print("I gave you $" + str(money_have))
    money_have = 0


def fill_action():
    global water_cap
    global coffee_cap
    global money_have
    global milk_cap
    global disposable_cups
    added_water = int(input("how many ml of water do you want to add:"))
    added_milk = int(input("how many ml of milk do you want to add:"))
    added_coffee = int(input("how many grams of coffee beans do you want to add:"))
    added_disposable = int(input("how many disposable cups of coffee do you want to add:"))
    water_cap = water_cap + added_water
    milk_cap = milk_cap + added_milk
    coffee_cap = coffee_cap + added_coffee
    disposable_cups = disposable_cups + added_disposable


def remaining_action():
    global water_cap
    global coffee_cap
    global money_have
    global milk_cap
    global disposable_cups
    print("The coffee machine has:")
    print(str(water_cap) + " of water")
    print(str(milk_cap) + " of milk")
    print(str(coffee_cap) + " of coffee beans")
    print(str(disposable_cups) + " of disposable cups")
    print("$" + str(money_have) + " of money")


while True:
    input_ = input("Write action (buy, fill, take, remaining, exit):")
    print()
    if input_ == "buy":
        buy_action()
        print()
    elif input_ == "fill":
        fill_action()
        print()
    elif input_ == "remaining":
        remaining_action()
        print()
    elif input_ == "take":
        take_action()
        print()
    else:
        break

    # num = input("Write how many cups of coffee you will need:")

# if int(num) == cup_pos:
#    print("Yes, I can buy make that amount of coffee")
# elif int(num) < cup_pos:
#    print("Yes, I can make that amount of coffee" "(" "and even " +str(cup_pos - int(num)) + "more than that" ")")
# else:
#    print("No, I can make only" + str(cup_pos) +  "cups of coffee")






