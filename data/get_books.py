from data.find_book import get_gr
from data.scrape_books import open_isbn_file
import time
import unicodecsv as csv
from data.timeout import timeout

"""
call API(GR, GBook, NLB) and store in database: book_title, authors, description(300), cover (can be null), pub_year, src
genre



"""



def store_books_in_csv(bks):
    """ finish scraping and put in dictionary then create csv"""

    with open('books.csv', 'wb') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(bks)
    return

@timeout(12)
def call_api(isbn):
    return get_gr(isbn)


def get_books():
    # create text files of 1000 isbns. do batch by batch.
    isbn_list = open_isbn_file()[:5000]
    bks = []
    i, j, t = 0, 0, 0 # i: valid, j: invalid, t: timeout count
    for isbn in isbn_list:
        print("Trying isbn: {}".format(isbn))
        try:
            bk=call_api(isbn)
        except:
            print("timeout likely {}".format(str(isbn)))
            t+=1
            continue
        time.sleep(1) # might be enough for not being banned

        if not bk:
            j+=1
        else:
            i += 1
            #bks.append(bk) for csv method
            store_book(bk)

        print("i: {} j: {} t: {}".format(str(i), str(j), str(t)))


    return bks

#bks=get_books()
#store_books_in_csv(bks)
