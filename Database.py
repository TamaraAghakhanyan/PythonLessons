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

cursor = connection.cursor()

cursor.execute('''create table mystaff.employees
      (id int primary key not null,
       first_name varchar(25) not null,
       last_name varchar(25) not null,
       department varchar(25) not null,
       phone varchar(25),
       address varchar(50),
       salary int);''')

connection.commit()
connection.close()

# to check out the content of the table:
# \d <schema name>.<table name>;

# to issue a query to see to see the rows/data inside the table:
# select * from <schema name>.<table name>;

# to insert a data inside the table:
# cursor.execute("insert into mystaff.employees (id,first_name,last_name,department,phone,address,salary) \
#  values (1, 'John', 'Smith', 'Sales', '0123456789', '1st Street, Miami', 50000), \
#         (2, 'Jack', 'Doe', 'IT', '0213456742', '2nd Street, NY', 55000), \
#         (3, 'Emily', 'Davids', 'Sales', '0123456999', '3rd Street, LA', 59000), \
#         (4, 'Karen', 'Willson', 'Logistics', '0823556785', '4th Street, Las Vegas', 41000), \
#         (5, 'Emma', 'Richard', 'Marketing', '0423453580', '5th Street, Denver', 40000);")
#
# connection.commit()
#
# connection.close()