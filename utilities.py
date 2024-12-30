import sqlite3

# Function to validate user input
def get_valid_choice(i):
    while True:
        try:
            user_input = int(input("Enter the number of your choice: "))
            if 1 <= user_input <= len(i):
                return user_input
            else:
                print(f"Please enter a number between 1 and {len(i)}.")
        except ValueError:
            print("Invalid input. Please enter a number.")


# Function to query the database
class Database:

    def __init__(self, db_name): # incase multiple database' can query whichever
        self.db_name = db_name

    def query_table(self, table_name, column_name, min_value): # define which table, column and value to search
        # Connect to the database
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()
        
        # Construct the SQL query dynamically
        query = f"SELECT * FROM {table_name} WHERE {column_name} >= ?"
        
        try:
            # Execute the query with the parameter
            cursor.execute(query, (min_value,))
            # Fetch and return the results
            results = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            results = []
        finally:
            # Close the connection
            connection.close()
        
        return results

    def query_table_with_conditions(self, table_name, conditions): #query with multiple conditions
        """
        Query a table with multiple conditions.
        :param table_name: The name of the table.
        :param conditions: A dictionary where keys are column names and values are the desired values.
        :return: List of rows matching the conditions.
        """
        # Connect to the database
        connection = sqlite3.connect(self.db_name)
        cursor = connection.cursor()

        # Construct the WHERE clause dynamically
        where_clause = " AND ".join([f"{column} = ?" for column in conditions.keys()])
        query = f"SELECT * FROM {table_name} WHERE {where_clause}"

        try:
            # Execute the query with parameters
            cursor.execute(query, tuple(conditions.values()))
            # Fetch and return the results
            results = cursor.fetchall()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
            results = []
        finally:
            # Close the connection
            connection.close()

        return results


# Query the 'items' table with the conditions
def print_query_conditions(table,conditions):

    # Query the 'items' table with the conditions
    items_results = db.query_table_with_conditions(table, conditions)
    for row in items_results:
        print(row)


#query database 
def print_query(table, attribute, value):
    results = db.query_table(table, attribute, value)
    numbered_list(results)
    #for row in results:
     #   print(row)


# Display numbered choices
def numbered_list(items):
    for index, i in enumerate(items, start=1):
        print(f"{index} -  {i}")


# set database
db = Database('Database.db')


# Testing
#print_query('spells','whm', 1) # query spells table for a column 'whm' with a value above 1
#print_query_conditions('items',{'name': 'Hatchet','owned': 1})
#print_query_conditions('items',{'elemental_damage_type': 'thunder', 'owned': 1})
#print_query('items','owned',1)
