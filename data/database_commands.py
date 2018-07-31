from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import pandas as pd

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

def create_book_csv():
    try:
        dbconfig = read_db_config()
        conn = MySQLConnection(**dbconfig)
        cursor = conn.cursor()
        # Execute the SQL command
        cursor.execute("SELECT * FROM book")
        # Fetch all the rows in a list of lists.
        ls=[]
        results = cursor.fetchall()
        c=0
        for row in results:
            new_record={}

            new_record['id']=row[0]
            new_record['book_title'] = row[1]
            new_record['authors'] = row[2]

            new_record['cover'] = row[3]
            new_record['pub_year'] = row[4]
            new_record['src'] = row[5]
            new_record['genre'] = row[6]
            new_record['description'] = row[7]
            print(new_record)
            print(len(row))
            ls.append(new_record)

        df = pd.DataFrame(ls,columns=['id','book_title','authors',
                                   'cover', 'pub_year','src','genre','description'])
        df.to_csv('set3.csv')

        while row is not None:
            row = cursor.fetchone()


    finally:
        cursor.close()
        conn.close()


def query_with_fetchmany():
    try:
        query_db("SELECT book_title FROM book")

        for row in iter_row(cursor, 10):
            #row is type tuple
            print(row)

    except Error as e:
        print(e)
    return


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



def convert_db_to_csv(db):
    pass

if __name__ == '__main__':
    #bk = {"book_title":"derp", "authors":"lek", "description":"d", "cover":"meh","pub_year":6789, "src":"gr", "genre":"art"}

    #print(replace_inverted_comma("i'm fine"))
    create_book_csv()
    #store_book(bk)