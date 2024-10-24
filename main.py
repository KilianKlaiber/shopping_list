import csv
import database

# Create a database of grocery products:

with database.connect_db() as connection:
    cursor = connection.cursor()
    SQL_Query = """ CREATE TABLE IF NOT EXISTS products(
        id SERIAL PRIMARY KEY,
        name VARCHAR(100) UNIQUE NOT NULL,
        category VARCHAR(100),
        description TEXT
    )
    """
    cursor.execute(SQL_Query)
    connection.commit()
    

# Enter Groceries from csv-file into database

with database.connect_db() as connection:
    cursor = connection.cursor()
    with open('groceries_list.csv','r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            insert_query = f"""INSERT INTO products(name, category, description)
            VALUES ('{row['Item']}','{row['Type']}','{row['Description']}')"""
                
            cursor.execute(insert_query)
            connection.commit()