# Command for creating a local postgreSQL database containing the products from which to chose for the shopping list.

import psycopg2
import os

PASSWORD = os.getenv("PASSWORD")


def main():

    pass


def connect_db() -> object:
    """Connect to Shopping List

    Returns:
        object: connection to the database Shopping list.
    """

    with psycopg2.connect(
        dbname="shopping_list",
        user="postgres",
        password=PASSWORD,
        host="localhost",
        port=5432,
    ) as connection:

        return connection


def create_grocery_table(grocery: str) -> None:
    """Create a table for groceries, such as apples
    
    The grocery table comprises the following columns:
    
    product_id: 1
    name: Granny Smith,
    brand: Elbe Obst,
    amount: 500,
    measure: gram,
    price: 5,
    cost_amount_ratio: 0.01,
    description: 'The Granny Smith, also known as a green apple or sour apple, is an apple cultivar that originated in Australia in 1868.'
    image: 
    


    Args:
        grocery (str): Name of the grocery (table)

    """

    with connect_db() as connection:
        cursor = connection.cursor()

        SQL_Query = f"""CREATE TABLE IF NOT EXISTS {grocery} (
                {grocery}_id serial PRIMARY KEY,
                product_id integer REFERENCES products(id),
                name VARCHAR(100) NOT NULL,
                brand VARCHAR(100) NOT NULL,
                amount FLOAT NOT NULL,
                measure VARCHAR(100) NOT NULL,
                price FLOAT NOT NULL,
                cost_amount_ratio FLOAT NOT NULL,
                description TEXT,
                image BYTEA);"""

        cursor.execute(SQL_Query)
        connection.commit()


def insert_image(grocery: str, grocery_id: str, image: bytes):
    """Insert image into record

    Args:
        grocery (str): _description_
        grocery_id (str): _description_
        image (bytes): _description_
    """
    with connect_db() as connection:
        cursor = connection.cursor()

        SQL_query = f"UPDATE {grocery} SET image = %s WHERE {grocery}_id = %s"
        cursor.execute(SQL_query, (psycopg2.Binary(image), grocery_id))
        connection.commit()


def insert_description(grocery: str, grocery_id: str, description: str):
    """Insert image into record

    Args:
        grocery (str): _description_
        grocery_id (str): _description_
        image (bytes): _description_
    """
    with connect_db() as connection:
        cursor = connection.cursor()

        SQL_query = f"UPDATE {grocery} SET description = %s WHERE {grocery}_id = %s"
        cursor.execute(SQL_query, (description, grocery_id))
        connection.commit()


def insert_grocery(
    grocery_table: str,
    grocery_name: str,
    brand: str,
    amount: float,
    measure: str,
    price: float,
    description: str = None,
    image: bytes = None,
) -> None:

    cost_amount_ratio = round(price / amount, 2)

    SQL_Query = f"""
    INSERT INTO {grocery_table} (
        grocery_name,
        brand,
        amount,
        measure,
        price,
        cost_amount_ratio,
        description) VALUES (%s, %s, %s, %s, %s, %s);
        """

    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(
            SQL_Query,
            (grocery_name, brand, amount, measure, price, cost_amount_ratio),
        )
        connection.commit()

    # Inset an image, if it exists:
    if image != None:
        
        # Retrieve the ID of the product
        SQL_Query = f"""
        SELECT {grocery_table}_id
        FROM grocery_table
        WHERE grocery_name = {grocery_name} AND brand = {brand};"""
        
        with connect_db() as connection:
            cursor = connection.cursor()
            cursor.execute(SQL_Query)
            results = cursor.fetchall()
            # Result is a list of tuples with a single item
            grocery_id = results[0][0]
        
        insert_image(grocery_table, grocery_id, image)
    
    # Insert a description, if it exists:
    if description != None:
        
        # Retrieve the ID of the product
        SQL_Query = f"""
        SELECT {grocery_table}_id
        FROM grocery_table
        WHERE grocery_name = {grocery_name} AND brand = {brand};"""
        
        with connect_db() as connection:
            cursor = connection.cursor()
            cursor.execute(SQL_Query)
            results = cursor.fetchall()
            # Result is a list of tuples with a single item
            grocery_id = results[0][0]
        
        insert_description(grocery_table, grocery_id, image)

if __name__ == "__main__":
    main()
