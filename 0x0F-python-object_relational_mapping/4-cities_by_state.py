#!/usr/bin/python3
"""2-my_filter_states"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    sqldb = MySQLdb.connect(host='localhost',
                            port=3306,
                            user=argv[1],
                            password=argv[2],
                            database=argv[3])
    cursor = sqldb.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM \
        cities JOIN states ON cities.state_id = states.id")
    row = cursor.fetchall()
    for i in row:
        print(i)
    cursor.close()
    sqldb.close()
