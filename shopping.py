import database
import PySimpleGUI as psg


def main():
    result = create_shopping_list()
    print(result)


def create_shopping_list() -> list:

    shopping_list = []

    decision = "yes"

    while decision == "yes":
        grocery = psg.popup_get_text("What do you want?", title=" Buy grocery")
        
        if grocery == None:
            decision = "no"
        else:
            grocery = grocery.lower()

        groceries = database.get_availabe_groceries()

        if grocery not in groceries and grocery != None:

            decision = psg.popup_yes_no(
                f"We do not have {grocery}\n Would you like something else?",
                title="What Else?",
            )
            decision = decision.lower()

            if decision == "no":
                print("So long!")
                return shopping_list
            else:
                decision = "yes"

        elif grocery != None:
            grocery_list = get_grocery(grocery)

            # Display Groceries in pop up window:
            # Sample data for the table
            data = [list(grocery_list[0]), list(grocery_list[1]), list(grocery_list[2])]
            # Table headings
            headings = ["Name", "Brand", "Price/Kg"]
            # Define the layout
            layout = [
                [
                    psg.Text(heading, size=(15, 1), justification="center")
                    for heading in headings
                ]
            ]  # Header row

            for i, row in enumerate(data):
                row_layout = [
                    psg.Text(row[0], size=(15, 1), justification="left"),
                    psg.Text(row[1], size=(15, 1), justification="left"),
                    psg.Text(row[2], size=(15, 1), justification="centre"),
                    psg.Button("OK", key=f"OK_{i}"),  # Unique key for each button
                ]
                layout.append(row_layout)

            # Create the window
            window = psg.Window("Chose your grocery", layout)

            # Event loop
            while True:
                event, _ = window.read()
                if event == psg.WINDOW_CLOSED or event in ["OK_0", "OK_1", "OK_2"]:
                    break

            window.close()

            choice = int(event[-1])
            
            

            amount = psg.popup_get_text(f"How much {grocery} do you want? (in Kg)")
            
            if amount != None:
                amount = float(amount)
                price = amount * grocery_list[choice][2]
                grocery_list = list(grocery_list[choice])
                grocery_list.append(amount)
                grocery_list.append(price)
                grocery_list.insert(0, grocery)
                shopping_list.append(grocery_list)

            return shopping_list



def get_grocery(grocery: str) -> list:

    with database.connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            f"SELECT name, brand, cost_amount_ratio FROM {grocery} ORDER BY cost_amount_ratio"
        )
        result = cursor.fetchall()

        return result


if __name__ == "__main__":
    main()
