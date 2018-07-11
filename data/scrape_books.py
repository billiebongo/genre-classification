

# create list of ISBNs in text file
# call each isbn, record hit and misses, written to csv

# store data iin mySQL





def check_digit(number):
    try:
        numberreal = number
        #keeps real number with "-"
        numberzero = number
        #this makes sure python doesnt drop the first 0 if it is at the start
        number = number
        number = int(number)
        number = str(numberzero)
        print("The ISBN Number Entered is", numberreal)
        num = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
        num = num%11
        checknum = 11 - num

        print("The Check Digit Should Be", checknum, "and the one in the code provided was", number[9])
        if int(checknum) == int(number[9]):
            print("The Check Digit Provided Is Correct")
            return True
        else:
            print("The Check Digit Provided Is Incorrect")
            return False
    except ValueError:
        print("Not Valid Number")

    except IndexError:
        print("Not 10 Digits")



def write_to_file(validated_isbn):
    print(validated_isbn)
    with open('isbn_list.txt', 'w') as f:
        f.write(','.join(validated_isbn))
    f.close()
def open_isbn_file():
    with open('isbn_list.txt', 'r') as f:
        line=f.readlines()
    print(line)
    list_of_isbn = line[0].split(",")
    return list_of_isbn

def generate_isbn_list():
    """write ISBNs to text file"""
    validated_isbn = []
    for i in range(1250107814, 1250740000):
        if check_digit(i):
            validated_isbn.append(str(i))
        else:
            continue

    write_to_file(validated_isbn)



def call_books_api():
    for isbn in isbns:
        book = find_book(isbn)



if __name__ == '__main__':
    generate_isbn_list()
    print(open_isbn_file())
