import mysql.connector

# Replace these values with your database credentials
host = "172.19.0.2"
user = "root"
password = "INZP4rdO9G"
port = 3306
database = "test"

# Create a connection
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    port=port,
    database=database
)

cursor = connection.cursor()

# Replace 'your_table_name' with the name of your table
table_name = "person"

# Example data
data_to_insert = {
    'PersonID': 123,
    'LastName': 'Sharma',
    'FirstName': 'Bhoopesh',
    'Address': 'def Colony',
    'City': 'Noida'
    # Add more columns and values as needed
}

# Prepare the INSERT statement
insert_query = f"INSERT INTO {table_name} ({', '.join(data_to_insert.keys())}) VALUES ({', '.join(['%s'] * len(data_to_insert))})"

# Execute the INSERT statement with the data
cursor.execute(insert_query, tuple(data_to_insert.values()))

# Commit the changes to the database
connection.commit()

# Close the cursor and the database connection
cursor.close()
connection.close()
