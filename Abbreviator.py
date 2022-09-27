#!/usr/bin/python

import sqlite3

import cursor as cursor
import table as table

# This is an external dependency, may need to be installed via command line
from pip._vendor.distlib.compat import raw_input

# Connects to our database
conn = sqlite3.connect('test.db')

# Alias to clean up queries
c = conn.cursor()

# Output to ensure we opened DB correctly
print("Opened database successfully")


# Define a function to get data from DB
def get_data():     # Defining this as a function will make the queries look much cleaner
    with conn:
        c.execute("SELECT * FROM WORDS")


programRunning = True

# While there is user input, keep running
while programRunning:
    # Print a user Menu
    print("""
    1. Add new Abbreviation
    2. Delete Abbreviation
    3. Show Abbreviations
    4. Quit
    """)

    # Initialize variables to hold inputs
    ans = raw_input("Make a selection\n")
    user_input = "input"

    # Input 1 adds abbreviations
    if ans == "1":
        abrv = raw_input("What is the abbreviation?")
        result = c.fetchone()
        if result:
            # record already exists
            print("Record already exists")
        else:
            long = raw_input("What is the full phrase of the abbreviation?")
            # We need to structure the query to translate user inputs
            query = ('INSERT INTO WORDS (ABRV, Long) '
                     'VALUES (:ABRV, :Long);')
            # Add the parameter mask to the query
            params = {
                'ABRV': abrv,
                'Long': long
            }
            # Commit changes and close connection
            conn.commit()

        print("Abbreviation Added")

    # Input 2 deletes abbreviations
    elif ans == "2":
        # Prints abbreviations so user can see what is in the DB
        cursor = conn.execute("SELECT * from WORDS")
        print(cursor.fetchall())
        # Ask the user what they want to delete
        abrv = (raw_input("What abbreviation would you like to delete?:"),)
        # Ensure we have what the user wants to delete in the DB
        result = cursor.fetchone()

        # if we find the abbreviation delete it
        if result:
            query = ('DELETE from WORDS (ABRV) '
                     'VALUES (:ABRV);')
            # Add the parameter mask to the query
            params = {
                'ABRV': abrv
            }
            # Delete record
            conn.commit()
            print("Record deleted")
        else:
            # If we don't find a record, then it probably isn't there
            print("Abbreviation not present in database, try again.")

    # Input 3 prints out the abbreviations
    elif ans == "3":
        print("Abbreviation Found")
        cursor = conn.execute("SELECT * from WORDS")
        print(cursor.fetchall())

        conn.close()
    # Input 4 closes program
    elif ans == "4":
        print("Goodbye")
        # Set our boolean to false to close the program
        programRunning = False

    # Anything else is invalid
    elif ans != "":
        print("\n **Not Valid Choice, please try again**")


