import csv
import database


def create_shopping_list() -> list:

    shopping_list = []

    decision = "yes"

    while decision == "yes":
        grocery = input("What do you want to buy? ")

        grocery = grocery.lower()

        groceries = database.get_availabe_groceries()

        if grocery not in groceries:
            print(f"We do not have {grocery}.")
            decision = input("Would you like something else? (Yes/No): ")
            decision = decision.lower()

            if decision == "no":
                print("So long!")
                return shopping_list
            else:
                decision = "yes"

        else:
            grocery_list = get_grocery(grocery)
            print(grocery_list[0:3])
            choice = int(input(f"Which {grocery} do you want? (0/1/2)"))
            amount = int(input(f"How much {grocery} do you want? (in Kg)"))
            price = amount * grocery_list[choice][2]
            grocery_list = list(grocery_list[choice])
            grocery_list.append(amount)
            grocery_list.append(price)
            shopping_list.append(grocery_list)

            decision = input("Would you like something else? (Yes/No)")
            decision = decision.lower()

            if decision == "no":

                total_price = 0
                for item in shopping_list:
                    total_price += item[4]

                total_price = round(total_price, 2)

                return shopping_list, total_price


def get_grocery(grocery: str) -> list:

    with database.connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT name, brand, cost_amount_ratio FROM {grocery} ORDER BY cost_amount_ratio"
        )
        result = cursor.fetchall()

        return result
