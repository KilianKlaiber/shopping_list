# Create a relational table for apples. 
# Amount is the weight in Kg

import database

with database.connect_db() as connection:
    cursor = connection.cursor()
    SQL_Query = """ CREATE TABLE IF NOT EXISTS apple (
        apple_id serial PRIMARY KEY, product_id integer REFERENCES products(id),
        name VARCHAR(100) NOT NULL,
        brand VARCHAR(100),
        amount FLOAT NOT NULL,
        price FLOAT NOT NULL,
        cost_amount_ratio FLOAT NOT NULL,
        description TEXT);
        """
    cursor.execute(SQL_Query)
    connection.commit()
