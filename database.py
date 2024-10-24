# Command for creating a local postgreSQL database containing the products from which to chose for the shopping list.

import psycopg2


def connect_db() -> object:

    with psycopg2.connect(
                dbname = 'shopping_list',
                user = 'postgres',
                password = 'kk452880',
                host = 'localhost',
                port = 5432
                
            ) as connection:
        
        return connection
