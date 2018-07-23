import os
print(os.listdir())

from find_book import get_gr
from isbn_file_handler import open_isbn_file
import time
from timeout import timeout
from database_commands import insert_book
"""
call API(GR, GBook, NLB) and store in database: book_title, authors, description(300), cover (can be null), pub_year, src
genre



"""

TIMEOUT = 15
"""
#def store_books_in_csv(bks):
#    finish scraping a list of books and put in dictionary then create csv

    with open('books.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(bks)
    return
"""
@timeout(TIMEOUT)
def retrieve_book(isbn):
    """
    wrapper function for timing out actlly
    """

    return get_gr(isbn)


def get_books():
    """
    return list, bks, of dictionaries
    """
    isbn_list = open_isbn_file()

    i, j, t = 0, 0, 0 # i: valid, j: invalid, t: timeout count

    for isbn in isbn_list:
        if len(str(isbn))==8:
            isbn = "00"+str(isbn)
        elif len(str(isbn)) == 9:
            isbn = "0"+str(isbn)
        elif len(str(isbn)) == 10:
            isbn=str(isbn)
        else:
            raise
        print("Trying isbn: {}".format(isbn))

        try:
            bk=retrieve_book(isbn)
        except Exception as e:
            print(e)
            print("timeout likely {}".format(isbn))
            t+=1
            continue
        time.sleep(1) # might be enough for not being banned

        if not bk:
            j += 1 #book not found
        else:
            i += 1 # book found
            try:
                insert_book(bk)
            except Exception as e:
                print(e)

        print("i: {} j: {} t: {}".format(str(i), str(j), str(t)))


    return

if __name__ == '__main__':
    print("============Run 6============")

    get_books()

