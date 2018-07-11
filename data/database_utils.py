
#http://www.mysqltutorial.org/python-connecting-mysql-databases/
#sudo apt-get install python3-mysql.connector



import mysql.connector
from mysql.connector import Error


def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database='genre_nlp',
                                       user='root',
                                       password='password')
        print(conn.is_connected())
        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()


if __name__ == '__main__':
    connect()

#class Book(object):
