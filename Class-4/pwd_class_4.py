# -*- coding: utf-8 -*-
"""PWD Class 4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cK5PumL-b-Liwe4f16kFgBLY4NuASh4f

# Part 1: Exploring Python tuples

1. Let's explore the use of a tuple in Python. The following tuple includes three elements.
"""

# A tuple is a collection which is ordered and unchangeable.

tuple = ("Stelios","Mary","Nick")

"""2. The next script exports the first element of your tuple."""

print(tuple[0])

"""3. You can use a for loop to extract the elements of a tuple as follows."""

for name in tuple:
  print(name)

"""4. You can combine lists and tuples. The following script creates an array of two tuples, where each tuple includes two sub-elements. """

# Index:        0                   1 
# Sub-index: 0        1          0      1

data = [("Stelios","London"),("Mary","Athens")]

"""5. You can print the first element of the data using the following script. This will print the element of index 0."""

data[0]

"""6. Now, print `Stelios` using the appropriate index numbers."""

data[0][0]

"""7. Let's export the data using the appropriate index numbers in a for loop."""

for record in data:
  print(record[0],"-",record[1])

"""> MySQL always returns results in the form of tuples, so always refer to the previous steps on how to manipulate tuple data.

# Part 2: Exploring MySQL with Python

In this tutorial we will use Python to connect to the MySQL and run our queries.

1. The first step is to install the MySQL connector. Whenever you run MySQL connections in Google Colab, you will need to install the appropriate connector.
"""

!pip install mysql.connector

"""2. Now the connector is installed we can `import` it and use it. We can also import the Error package to help us explore issues while running our scripts."""

import mysql.connector
from mysql.connector import Error

"""3. Let's create a new server connection. The next script develops a function that creates a new connector. As you can see the script is totally customisable to your own MySQL server.

> The try - except script will show an error if there is a connection problem.

> Make sure you adjust the `host`,`user` and `password` to your own configurations based on your MySQL server.
"""

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

host = "IP_ADDRESS" # Add here your host IP address from the GCP
user = "root"
password = "1234" # Add here your password

connection = create_server_connection(host, user, password)

"""4. Let's create a cursor that allows row-by-row processing of the result sets. The next script creates a new database called `music_db`."""

cursor = connection.cursor()
cursor.execute("CREATE DATABASE music_db")
print("Database created successfully")

"""5. Now, let's create a new connection to the `music_db` database. As you can see the `create_db_connection` function also accepts the `db_name`."""

def create_db_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("MySQL Database connection successful")
    except Error as err:
        print(f"Error: '{err}'")

    return connection

"""6. Now time to connect to the `music_db`. Make sure you adjust `host` and `password` one more time."""

host = "IP_ADDRESS"
user = "root"
password = "1234"  
database = "music_db"

connection = create_db_connection(host, user, password,database)

"""7. Create a new table called `instruments`. The table has five attributes as follows."""

create_instruments_table = """
CREATE TABLE instruments (
  instrument_id INT PRIMARY KEY,
  instrument_title VARCHAR(40) NOT NULL,
  instrument_description TEXT NOT NULL,
  instrument_type TEXT NOT NULL,
  instrument_cost FLOAT NOT NULL
  );
 """

"""8. Then, you have to create a cursor to run the query and commit the results."""

cursor = connection.cursor()
cursor.execute(create_instruments_table)
connection.commit()
print("Query successful")

"""9. Now, create the `customers` table."""

create_customer_table = """
CREATE TABLE customers (
  customer_id INT PRIMARY KEY,
  customer_first_name VARCHAR(40) NOT NULL,
  customer_last_name VARCHAR(40) NOT NULL,
  customer_email VARCHAR(40) NOT NULL,
  customer_dob DATE,
  phone_no VARCHAR(20)
  );
 """

"""> This is a supporting scipt, in case fo an error, you can drop the table using the next command.

> **Do not run this command.**
"""

# cursor = connection.cursor()
# cursor.execute("DROP TABLE instruments;")
# print("Database created successfully")

"""10. The next script creates a function to allow you to execute queries. The function accepts a `connection` and the `query`."""

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query successful")
    except Error as err:
        print(f"Error: '{err}'")

"""11. Let's use the function to connect and run the `create_customer_table`."""

execute_query(connection,create_customer_table)

"""12. Now, let's run the `SHOW DATABASES` command."""

cursor = connection.cursor()
cursor.execute("SHOW DATABASES;")

for (databases) in cursor:
     print(databases[0])

"""13. Now, let's run the `SHOW TABLES` command."""

cursor = connection.cursor()
cursor.execute("SHOW TABLES;")

for (databases) in cursor:
     print(databases[0])

"""14. Time to create a new table. You can first create a variable to store the query text."""

create_order_table = """
CREATE TABLE orders (
  customer_id INT,
  instrument_id INT,
  oder_date DATE,
  PRIMARY KEY(customer_id,instrument_id),
  CONSTRAINT FK1 FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  CONSTRAINT FK2 FOREIGN KEY (instrument_id) REFERENCES instruments(instrument_id)
  );
 """

"""15. Then execute the query."""

execute_query(connection,create_order_table)

"""16. Now, let us populate the data for both `instruments`, `customers` and `orders`."""

pop_instruments = """
INSERT INTO instruments VALUES
(1,  'Guitar', 'A Gibson Les Paul guitar, a fretted musical instrument that typically has six strings. ', 'Chordophone', 1500),
(2,  'Guitar', 'A Fender Telecaster guitar, played by strumming or plucking the strings with the dominant hand', 'Chordophone', 100),
(3,  'Piccolo', 'A Yamaha highest-pitched woodwind instrument of orchestras and military bands.', 'Woodwind', 1200),
(4,  'Drum', 'A Pearl drum, a member of the percussion group of musical instruments', 'Membranophones', 600),
(5,  'Saxophone', 'A Selmer saxophone with a conical body, usually made of brass. ', 'Woodwind ', 800);
"""

execute_query(connection, pop_instruments)

pop_customers = """
INSERT INTO customers VALUES
(101, 'Mary', 'James', 'mary.james@pwd.com','1990-04-15','0712387436'),
(102, 'Nick', 'Oliver', 'nick.oliver@pwd.com','1985-06-11','0783002133'),
(103, 'Mary', 'Clark', 'mary.clark@pwd.com','2000-11-02','0701239936'),
(104, 'Tom', 'Mack', 'tom.mack@pwd.com','1993-11-12','0728469112'),
(105, 'Tim', 'James', 'tim.james@pwd.com','1996-10-12','0740117291');
"""

execute_query(connection, pop_customers)

pop_orders = """
INSERT INTO orders VALUES
(101,1,'2022-10-11'),
(101,2,'2022-10-11'),
(103,3,'2022-10-11'),
(104,4,'2022-10-11'),
(103,4,'2022-10-11'),
(105,4,'2022-10-11'),
(102,5,'2022-10-11'),
(101,5,'2022-10-11');
"""

execute_query(connection, pop_orders)

"""17. Create a new query to retrieve customer data."""

query = """
SELECT *
FROM customers;
"""

cursor.execute(query)
results = cursor.fetchall()

for result in results:
  print(result)

"""18. Run the next query to export firstname and surname from your customers"""

query = """
SELECT customer_first_name,customer_last_name
FROM customers;
"""

cursor.execute(query)
results = cursor.fetchall()

for result in results:
  print("First name:",result[0]," - Surname",result[1])

"""19. The next code creates a read query function. The function accepts the connection and the query and it runs it."""

def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as err:
        print(f"Error: '{err}'")

"""20. The next query retrieves customer first name, last name and instrument title."""

query1 = """
SELECT customer_first_name,customer_last_name,instrument_title
FROM customers,orders,instruments
WHERE 
customers.customer_id=orders.customer_id
AND
instruments.instrument_id=orders.instrument_id;
"""
results = read_query(connection, query1)

for result in results:
  print(result)

"""21. The next query counts the amount of instruments in the intruments table."""

query2 = """
SELECT instrument_title,count(instrument_title)
FROM customers,orders,instruments
WHERE 
customers.customer_id=orders.customer_id
AND
instruments.instrument_id=orders.instrument_id
GROUP BY instrument_title;
"""
results = read_query(connection, query2)

for result in results:
  print(result)

"""22. How many instruments have been ordered by Mary James?"""

query3 = """
SELECT customer_first_name,customer_last_name,count(customer_last_name)
FROM customers,orders,instruments
WHERE 
customers.customer_id=orders.customer_id
AND
instruments.instrument_id=orders.instrument_id
AND customers.customer_first_name='Mary'
AND customers.customer_last_name='James';
"""
results = read_query(connection, query3)

for result in results:
  print(result)

"""23. The next function counts how many instruments exist per person."""

def countIntrumentsPerPerson(first_name,last_name):
  query = """
  SELECT customer_first_name,customer_last_name,count(customer_last_name)
  FROM customers,orders,instruments
  WHERE 
  customers.customer_id=orders.customer_id
  AND
  instruments.instrument_id=orders.instrument_id
  AND customers.customer_first_name=%s
  AND customers.customer_last_name=%s;
  """
  cursor.execute(query,(first_name,last_name))
  result = cursor.fetchall()
  return result[0][2]

"""24. Let's use the function."""

first_name = input("What is the customer's first name? ")
last_name = input("What is the customer's last name? ")

num_of_instruments = countIntrumentsPerPerson(first_name,last_name)

print(first_name,last_name,"ordered",num_of_instruments,"instrument(s)!")

"""25. Let's create a function to retrieve instruments per person."""

def showIntrumentsPerPerson(first_name,last_name):
  query = """
  SELECT instruments.instrument_title
  FROM customers,orders,instruments
  WHERE 
  customers.customer_id=orders.customer_id
  AND
  instruments.instrument_id=orders.instrument_id
  AND customers.customer_first_name=%s
  AND customers.customer_last_name=%s;
  """
  cursor.execute(query,(first_name,last_name))
  result = cursor.fetchall()
  return result

"""26. Let's use it."""

first_name = input("What is the customer's first name? ")
last_name = input("What is the customer's last name? ")

num_of_instruments = showIntrumentsPerPerson(first_name,last_name)

print(first_name,last_name,"ordered:",num_of_instruments)

"""27. Let's select all the data."""

query2 = """
SELECT instrument_title,instrument_cost FROM instruments;
"""
results = read_query(connection, query2)

for result in results:
  print(result)

"""28. Now, let's update a record. We need to update instrument with id=5 to a new price of 1000"""

update = """
UPDATE instruments 
SET instrument_cost = 100
WHERE instrument_id = 5;
"""
execute_query(connection, update)

"""29. Let's export the data to see the change."""

query2 = """
SELECT instrument_title,instrument_cost FROM instruments;
"""
results = read_query(connection, query2)

for result in results:
  print(result)

"""30. Finally, the next script deletes the data.

> First insert a new instrument.
"""

pop_instruments = """
INSERT INTO instruments VALUES
(6,  'Trumpet', 'The trumpet is a brass instrument commonly used in classical and jazz ensembles.', 'Brass ', 650);
"""

execute_query(connection, pop_instruments)

delete_instrument = """
DELETE FROM instruments WHERE instrument_id = 6;
"""

execute_query(connection, delete_instrument)