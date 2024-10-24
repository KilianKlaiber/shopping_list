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

"""
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname = 'postgres',
            user = 'postgres',
            password = 'kk452880',
            host = 'localhost',
            port = 5432
            
        )
        return conn
    
    except psycopg2.Error as e:
        print(f"An error occured while connection to db: {e}")
        return None
    
    except Exception as e:
        print(f"An unexpected error occured [e]")
        return None
"""