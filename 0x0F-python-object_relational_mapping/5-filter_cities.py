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
    arg = (argv[4], )
    exe = "SELECT cities.name FROM cities JOIN states ON\
    cities.state_id = states.id AND states.name = %s ORDER BY cities.id ASC"
    cursor.execute(exe, arg)
    row = cursor.fetchall()
    print(", ".join(i[0] for i in row))
    cursor.close()
    sqldb.close()
