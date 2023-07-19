# # PostgeSQL
#
# # To see the list of databases:
# \l
#
# # create database:
# CREATE USER <username> PASSWORD ‘password’;
#
# # To create role:
# \du
#
# # To grant the user all the necessary privileges:
# grant all privileges on database <database> to <username>;
#
# # To connect to database:
# \c <database> <username>;
#
# # to create schema:
# create schema <schema name> authorization <username>;
#
# # To see the schema inside the database:
# \dn
#
# # To delete the schema:
# drop schema <schema name>;
#
# # To delete the database/user you need to disconnect from the database:
# \c postgres;
# drop user <username>;
# drop database <database>;

# to verify if there is any table in schema:
# \dt <schema name>.*


# CONNECTING PYTHON TO DATABASE

# the code to connect to database:


import psycopg2
def print_hi():
    connection = psycopg2.connect(
        database="staff",
        user="postgres",
        password="postgres",
        host="localhost",  # If your database is on the same machine, use "localhost"
        port="5432"  # By default, PostgreSQL uses port 5432
        )
print("Connected to the database!")



try:
    connection = psycopg2.connect(
        database="staff",
        user="toma",
        password="python",
        host="localhost",    # If your database is on the same machine, use "localhost"
        port="5432"     # By default, PostgreSQL uses port 5432
    )
    print("Connected to the database!")

#     with connection.cursor() as cursor:
#
#         # Execute the SQL query to insert multiple rows
#         cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
#          values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
#                 (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
#                 (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
#                 (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
#                 (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")
#     connection.commit()
# #
    print("Records inserted successfully!")

except psycopg2.Error as e:
    print(f"Error connecting to the database: {e}")

cursor = connection.cursor()

# cursor.execute('''create table mystaff.employees
#       (id int primary key not null,
#        first_name varchar(25) not null,
#        last_name varchar(25) not null,
#        department varchar(25) not null,
#        phone varchar(25),
#        address varchar(50),
#        salary int);''')



# to check out the content of the table:
# \d <schema name>.<table name>;

# to issue a query to see to see the rows/data inside the table:
# select * from <schema name>.<table name>;

# to insert a data inside the table:
# see above lines 64-71

# to update records in the database:
# - to check the connection with the database
# - to initialize the cursor:
# cursor = connection.cursor()


# cursor = connection.cursor()
# cursor.execute("update mystaff.employees set department = 'Logistics' where last_name = 'Doe';")
# connection.commit()
# connection.close()

# # deleting records from the database
# cursor = connection.cursor()
# cursor.execute("delete from mystaff.employees where salary > 30000;")
# connection.commit()
# connection.close()

# QUERYING THE DATABASE WITH PYTHON
cursor = connection.cursor()
# getting the employees the salary of which is  > 50000:
# cursor.execute("select * from mystaff.employees where salary > 50000;")
# to fetch all the results of the above query and returns a list:
# records = cursor.fetchall()
# print(records)
# for record in records:
#     print(record)

# querying using BETWEEN keyword:
# cursor.execute("select * from mystaff.employees where salary between 40000 and 45000;")
# records = cursor.fetchall()
# print(records)
# for record in records:
#     print(record)

# querying using IN keyword:
# cursor.execute('''SELECT * FROM mystaff.employees WHERE department IN ('Sales', 'IT');''')
# records = cursor.fetchall()
# print(records)
# for record in records:
#     print(record)

# querying using LIKE keyword:
cursor.execute('''SELECT * FROM mystaff.employees WHERE last_name LIKE 'D%';''')
records = cursor.fetchall()
print(records)
for record in records:
    print(record)