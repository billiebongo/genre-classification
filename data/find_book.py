# scrape the books from goodreads and google books


import requests, re
from goodreads import client
from goodreads.request import GoodreadsRequestException

GOODREADS_API_KEY = "P6LBODEZy9wK0K8RnlXzA"
GOODREADS_API_SECRET = "xNOuHajksU3PCGNGXs5TIiiZZynFOAjgxHiMEsywY"

#GBOOKS_API_TOKEN = "AIzaSyDrl351Oxpu2r79QlnsWePkzrBg1re19Zw"
GBOOKS_API_TOKEN = "AIzaSyCRsJ0Zz-Egz6hcO90TZmRfIaoU5tHigEg"


gc = client.GoodreadsClient(GOODREADS_API_KEY, GOODREADS_API_SECRET)

# get genre based on popular shelves of GR

GENRE_LIST = ["children", "fantasy", "young-adult", "self-help", "religion", "math", "historical", "science", "health",
              "comics", "travel", "horror", "economics", \
              "business", "religion", "romance", "psychology", "computer-science", "philosophy", "humour", "finance",
              "mystery", "thriller", "chick-lit", "historical", "biography", "politics", "social-science", "entrepreneurship" \
                                                                                                "art", "cookbook",
              "drama", "adventure", "biology", "physics", "fiction", "non-fiction"]

NO_COVER = "NO_COVER"


def clean_html(raw_html):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', raw_html)
    return cleantext


def get_genre(pop_shelves):
    print(pop_shelves)
    for pop in pop_shelves:
        if (type(pop._shelf_dict) == 'string'):
            return "nil"
        if ((str(pop) == "to-read") or (str(pop) == "books-i-own") or (str(pop) == "currently-reading") or (
                str(pop) == "favorites")):
            continue
        for g in GENRE_LIST:
            if (str(pop) == g):
                print(g)
                return g
    return "nil"


def get_gbook(isbn):
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    payload = {
        'key': GBOOKS_API_TOKEN,
        'q': 'isbn:' + isbn
    }
    try:
        r = requests.get(BASE_URL, params=payload)
        r.raise_for_status()
        result = r.json()
        if (result['totalItems'] != 1):
            return None
        book = {}
        if "totalItems" in result and result['totalItems'] == 1:

            result = result['items'][0]['volumeInfo']

            if "industryIdentifiers" in result:
                isbn10 = [i for i in result['industryIdentifiers'] if i['type'] == 'ISBN_10']
                if len(isbn10) > 0:
                    book['isbn'] = isbn10[0]['identifier']
                isbn13 = [i for i in result['industryIdentifiers'] if i['type'] == 'ISBN_13']
                if (len(isbn13) > 0):
                    book['isbn13'] = isbn13[0]['identifier']
            if "title" in result:
                book['book_title'] = result['title']
            if "subtitle" in result:
                book['book_title'] += ': ' + result['subtitle']
            if "authors" in result:
                book['authors'] = result['authors']  # this is a list
            if "description" in result:
                book['description'] = result['description']
            else:
                book['description'] = ""
            if "publishedDate" in result:
                book['pub_year'] = result['publishedDate'][:4]
            else:
                book['pub_year'] = ""
            print(result)
            if "imageLinks" in result:
                print(result['imageLinks'])
                book['cover'] = result['imageLinks']['thumbnail']
                return result['imageLinks']['thumbnail']
            else:
                book['cover'] = NO_COVER

        # totalitems != 1
        return book

    except requests.exceptions.RequestException as e:
        print(e)
        return None

    except Exception as e:
        print(e)
        print(type(e))
        return None
    return None

"""
def get_gbook_photo(isbn):
    BASE_URL = 'https://www.googleapis.com/books/v1/volumes'
    payload = {
        'key': GBOOKS_API_TOKEN,
        'q': 'isbn:' + isbn
    }
    r = requests.get(BASE_URL, params=payload)
    r.raise_for_status()
    result = r.json()
    print(result)
    book = {}
    if "totalItems" in result and result['totalItems'] > 0:
        result = result['items'][0]['volumeInfo']
        if "imageLinks" in result:
            print(result['imageLinks'])
            return result['imageLinks']['thumbnail']
        else:
            print("both gr and gb no_cover")
            return NO_COVER
    return NO_COVER

"""
def get_gr(isbn):
    try:
        gr = gc.book(isbn=isbn)
        book = {}

        book['id'] = gr._book_dict['id']  # GR BOOK SHOULD HAVE ID
        book['src'] = "gr"
        book['book_title'] = gr.title
        if gr.isbn:
            print("gr give isbn")
            book['isbn'] = gr.isbn
        else:
            if len(isbn) == 10:
                book['isbn'] = isbn
            else:
                book['isbn'] = -1
        if gr.isbn13:
            book['isbn13'] = gr.isbn13
        else:
            if len(isbn) == 13:
                book['isbn13'] = isbn
            else:
                book['isbn13'] = -1
        book['cover'] = 'l'.join(gr.image_url.rsplit('m', 1))

        for items in gr.authors:
            print(items)
        book['authors'] = str(gr.authors)#[1:-1].split(', ')
        book['pub_year'] = gr.publication_date[2]
        if gr.description:
            book['description'] = clean_html(gr.description.replace('\n', '').replace('<br />', '\n'))
        else:
            book['description'] = ''

        # print(gr.popular_shelves)
        try:
            if gr.popular_shelves:

                print("printing:" + str(gr.popular_shelves))

                book['genre'] = get_genre(gr.popular_shelves)
            else:
                book['genre'] = "nil"
        except:
            book['genre'] = "nil"
        print(book['genre'])

    #raised if connectionError or isbn cannot be found
    except (GoodreadsRequestException) as e:
        """
        if GR fails, try GBooks
        """
        print("goodreads exception error")

        #book = get_gbook(isbn)

        #if book != None:
        #    print("here1")
        #    book['src'] = "gb"
        #    return book

        return None
    except (KeyError) as e:  # if gr dies
        print("Data received is lacking something")
        print(e)

        return None

    return book

if __name__ == "__main__":
    print(get_gr("0739405756"))

"""
Test cases:
-Book alr in DB, but edition(isbn10/13) is not
-Edition(isbn10/13) alr in DB
-normal ISBN10/13 found in GR
-ISBN10/13 found in gbooks not GR
-ISBN10/13 not found in gbooks and GR
-ISBN10/13 not found in GR and Gbooks, but book is actually in db
-Book with same name but diff author
-GR no photo, but gbooks got
-Gr and gbooks no photo, but gr site has
-gr and gbooks no photo and gr site dont have
-Book with same name and same author but actually diff books.
-GR API not avail, Gbooks is
-GR API and Gbooks API both not avail
-ISBN10/13 invalid format (why is this even POSTed)
-Book found but no ISBN10/13 returned by GR
-Book found but no DESCRIPTION/ISBN/AUTHORS whatsoever
-Genre not found
		#to test no isbn found:"7111111111111"
"""
