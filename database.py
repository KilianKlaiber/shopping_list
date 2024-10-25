# Command for creating a local postgreSQL database containing the products from which to chose for the shopping list.

import psycopg2
import os

PASSWORD = os.getenv('PASSWORD')

def main():
    
    insert_image()


def connect_db() -> object:
    """Connect to Shopping List

    Returns:
        object: connection to the database Shopping list.
    """

    with psycopg2.connect(
                dbname = 'shopping_list',
                user = 'postgres',
                password = PASSWORD,
                host = 'localhost',
                port = 5432
                
            ) as connection:
        
        return connection

def create_grocery_table(grocery: str) -> None:
    """ Create a table for groceries, such as apple
    
    Args:
        grocery (str): Name of the grocery (table)
    
    """
    
    with connect_db() as connection:
        cursor = connection.cursor()
        
        SQL_Query = f"""CREATE TABLE IF NOT EXISTS {grocery} (
                {grocery}_id serial PRIMARY KEY,
                product_id integer REFERENCES products(id),
                name VARCHAR(100) NOT NULL,
                brand VARCHAR(100),
                amount FLOAT NOT NULL,
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

def insert_grocery(
    grocery_table: str, 
    grocery_name: str, 
    brand: str, 
    amount: float, 
    price: float,
    description: str = None, 
    image: bytes = None)-> None:
    
    cost_amount_ratio = round(price/amount, 2)
    
    SQL_Query = f"""
    INSERT INTO {grocery_table} (
        grocery_name,
        brand,
        amount,
        price,
        cost_amount_ratio,
        description) VALUES (%s, %s, %s, %s, %s, %s);
        """
    
    with connect_db() as connection:
        cursor = connection.cursor()
        cursor.execute(SQL_Query, (grocery_name, brand, amount, price, cost_amount_ratio, description))
        connection.commit()



if __name__ == "__main__":
    main()