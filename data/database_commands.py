from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config

def query_db(query):
    dbconfig = read_db_config()
    conn = MySQLConnection(**dbconfig)
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    rows=cursor.fetchmany(10)
    print(rows)
    cursor.close()
    conn.close()
    return rows

def replace_inverted_comma(s):
    s=s.replace("'", "\\'")
    return s


def iter_row(cursor, size=10):
    while True:
        rows = cursor.fetchmany(size)
        if not rows:
            break
        for row in rows:
            yield row

def query_with_fetchone():
    try:

        query_db("SELECT * FROM books")
        row = cursor.fetchone()

        while row is not None:
            print(row[0])
            row = cursor.fetchone()

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def query_with_fetchmany():
    try:
        query_db("SELECT * FROM books")

        for row in iter_row(cursor, 10):
            #row is type tuple
            print(row)

    except Error as e:
        print(e)

    finally:
        cursor.close()
        conn.close()


def update_book(book_id, title):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE books
                SET title = %s
                WHERE id = %s """

    data = (title, book_id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_book(bk):
    #query = "INSERT INTO books(title,isbn) " \
     #       "VALUES(%s,%s)"
    #args = (title, isbn)
    #bk["description"] bk["book_title"] bk["authors"]

    if len(bk["description"])>1000:
        bk["description"] = bk["description"][:1000]

    if bk["pub_year"] == None:
        print("NONE!")
        bk["pub_year"] = 1



    data_list = [ replace_inverted_comma(bk["book_title"]), replace_inverted_comma(bk["authors"]), replace_inverted_comma(bk["description"]), replace_inverted_comma(bk["cover"]), bk["pub_year"], bk["src"], bk["genre"]]

    try:
        values = ["'%s'" % v for v in data_list]
        tail=", ".join(values)+");"
        query = "INSERT INTO book(book_title, authors,description, cover, pub_year, src, genre) VALUES ("+tail
        print(query)
        rows = query_db(query)
        for row in rows:
            # row is type tuple
            print(row)



        #if cursor.lastrowid:
        #    print('last insert id', cursor.lastrowid)
        #else:
        #    print('last insert id not found')
    except Error as e:
        print(e)
    return



def delete_books(book_ids):
    db_config = read_db_config()

    query = "DELETE FROM books WHERE id IN (3,4,5)"
    #query = "DELETE FROM books WHERE id > 19"

    try:
        # connect to the database server
        conn = MySQLConnection(**db_config)

        # execute the query
        cursor = conn.cursor()
        print(query)
        cursor.execute(query)#, book_ids)
        print("sss")
        print(cursor)
        # accept the change`
        conn.commit()

    except Error as error:
        print("er")
        print(error)

    finally:
        cursor.close()
        conn.close()


if __name__ == '__main__':
    #bk = {"book_title":"derp", "authors":"lek", "description":"d", "cover":"meh","pub_year":6789, "src":"gr", "genre":"art"}

    print(replace_inverted_comma("i'm fine"))

    #store_book(bk)