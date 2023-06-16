#!/usr/bin/python3
"""
Module that displays all values in the states table of hbtn_0e_0_usa
"""
import sys
import MySQLdb


def main():
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )

    search_name = sys.argv[4]
    # Create a cursor object
    cursor = db.cursor()
    
    # Create the SQL query using format
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"\
            .format(search_name)

    # Execute the SELECT statement
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
