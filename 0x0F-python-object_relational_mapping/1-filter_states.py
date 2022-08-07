#!/usr/bin/python3
"""1-filter_states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sqldb = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=argv[1],
                            password=argv[2],
                            database=argv[3])
    cursor = sqldb.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    row = cursor.fetchall()
    for i in row:
        print(i)
    cursor.close()
    sqldb.close()
