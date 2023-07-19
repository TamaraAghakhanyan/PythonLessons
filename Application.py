# MIGRATING RECORDS FROM TEXT FILE TO THE DATABASE

import psycopg2
# to open the text file:
f = open("/Users/tamaraaghakhanyan/Downloads/employees (1).txt")

# to create an empty list and to store the text file data in a form of list:
records = []

for i in f.readlines():
    records.append(i.split("/ "))

print(records)


# connecting to database:

try:
    connection = psycopg2.connect(
        database="staff",
        user="toma",
        password="python",
        host="localhost",    # If your database is on the same machine, use "localhost"
        port="5432"     # By default, PostgreSQL uses port 5432
    )
    print("Connected to the database!")

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")

cursor = connection.cursor()