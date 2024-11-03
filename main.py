import csv
import database

# Create a database of grocery products:


def main():

    id = get_id("Gut")

    print(id)


def get_id(grocery: str) -> int | None:
    """
    Retrieve the id of a particular grocery from products table
    Return None if grocery not in prodcuts table

    Args:
        grocery (str): Name of the grocery
    """

    with database.connect_db() as connection:
        cursor = connection.cursor()

        cursor.execute(f"SELECT id FROM products WHERE name = '{grocery}'")
        result = cursor.fetchall()

        if result == []:
            return None
        else:

            return result[0][0]


main()
""" 
database.create_grocery_table('Banana')


description =  "Chiquita bananas are known for their bright yellow skin, slightly curved shape, and consistent quality." \
    "They’re usually sweet, creamy, and soft when ripe, making them ideal for snacking, baking, and smoothies."

database.insert_grocery(
    grocery_table="Banana",
    grocery_name="Chiquita Banana",
    brand="Chiquita", 
    amount=1.5, 
    measure="Kg", 
    price=1.7,
   )

 """
