# Command for creating a local postgreSQL database containing the products from which to chose for the shopping list.

import psycopg2
import os

PASSWORD = os.getenv('PASSWORD')

def main():
    
    create_grocery_table('beans')


def connect_db() -> object:

    with psycopg2.connect(
                dbname = 'shopping_list',
                user = 'postgres',
                password = PASSWORD,
                host = 'localhost',
                port = 5432
                
            ) as connection:
        
        return connection

def create_grocery_table(grocery):
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
    with connect_db() as connection:
        cursor = connection.cursor()
        
        SQL_query = f"UPDATE {grocery} SET image = %s WHERE {grocery}_id = %s"
        cursor.execute(SQL_query, (psycopg2.Binary(image), grocery_id))
        connection.commit()

if __name__ == "__main__":
    main()