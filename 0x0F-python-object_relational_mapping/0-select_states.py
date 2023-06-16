#!/usr/bin/python3
"""
Moduule lists state in hbtn_0e_0_usa
"""
import MySQLdb
import sys


def main():
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user= sys.argv[1],
            passwd= sys.argv[2],
            db= sys.argv[3]
            )
    # Create a cursor object
    cursor = db.cursor()
    # Execute the SELECT statement
    query = "SELECT * FROM states ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
