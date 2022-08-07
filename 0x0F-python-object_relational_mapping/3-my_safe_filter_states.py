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
    sysargv = argv[4].split(';')
    name = sysargv[0].strip('"\'')
    cursor.execute("SELECT * FROM states WHERE BINARY name = '{}'"
                   .format(name))
    row = cursor.fetchall()
    for i in row:
        print(i)
    cursor.close()
    sqldb.close()
