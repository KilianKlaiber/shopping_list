import database
import PySimpleGUI as psg

def create_shopping_list() -> list:

    shopping_list = []

    decision = "yes"

    while decision == "yes":
        grocery = psg.popup_get_text('What do you want?', title=' Buy grocery')

        grocery = grocery.lower()

        groceries = database.get_availabe_groceries()

        if grocery not in groceries:
            
            decision = psg.popup_yes_no(f"We do not have {grocery}\n Would you like something else?", title= 'What Else?')
            decision = decision.lower()

            if decision == "no":
                print("So long!")
                return shopping_list
            else:
                decision = "yes"

        else:
            grocery_list = get_grocery(grocery)
            
            # Display Groceries in pop up window:
            
            data = [
                grocery_list[0],
                grocery_list[1],
                grocery_list[2]
            ]
            
            headings = ["Name", "Brand", "Price/Kg"]
            
            layout = [
                [psg.Text(grocery_list[0]), psg.OK()],
                [psg.Text(grocery_list[1]), psg.OK()],
                [psg.Text(grocery_list[2]), psg.OK()]
            ]
            window = psg.Window(f'CHose your apple {grocery}:', layout)
                        
            while True:
                event = window.read()
                print(event)
                
                if event == psg.WIN_CLOSED or event in ['OK', 'OK0', 'OK1']:
                    break
            window.close()
            
            print(grocery_list[0:3])
            choice = int(input(f"Which {grocery} do you want? (0/1/2)"))
            amount = int(input(f"How much {grocery} do you want? (in Kg)"))
            price = amount * grocery_list[choice][2]
            grocery_list = list(grocery_list[choice])
            grocery_list.append(amount)
            grocery_list.append(price)
            shopping_list.append(grocery_list)

            decision = psg.popup_yes_no(f"Would you like something else?", title= 'What Else?')

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
