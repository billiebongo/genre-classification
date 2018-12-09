
#http://www.mysqltutorial.org/python-connecting-mysql-databases/
#sudo apt-get install python3-mysql.connector



import mysql.connector
from mysql.connector import Error

DATABASE_NAME = 'genre_nlp'
DB_PW = 'password'

def connect():
    """ Connect to MySQL database """
    try:
        conn = mysql.connector.connect(host='localhost',
                                       database= DATABASE_NAME,
                                       user='root',port = 3306,
                                       password=DB_PW)

        if conn.is_connected():
            print('Connected to MySQL database')

    except Error as e:
        print(e)

    finally:
        conn.close()

if __name__ == '__main__':
    connect()

