

# create list of ISBNs in text file
# call each isbn, record hit and misses, written to csv

# store data iin mySQL

from isbn_runs import ISBN_LIST

"""
Generate list of isbns in a textfile
Script contains some textfile helper functions
"""

ISBN_LIST_FILE = 'isbn_list.txt'

def check_digit(number):
    try:
        numberreal = number
        #keeps real number with "-"
        numberzero = number
        #this makes sure python doesnt drop the first 0 if it is at the start
        number = number
        #number = int(number)
        number = str(numberzero)

        if len(number)==10:
            num = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
        elif len(number)==9:
            num = int(number[0]) * 9 + int(number[1]) * 8 + int(number[2]) * 7 + int(number[3]) * 6 + int(number[4]) * 5 + int(number[5]) * 4 + int(number[6]) * 3 + int(number[7]) * 2
        elif len(number) == 8:
            num = int(number[0]) * 8 + int(number[1]) * 7 + int(number[2]) * 6 + int(number[3]) * 5 + int(number[4]) * 4 + int(number[5]) * 3 + int(number[6]) * 2
        else:
            return
        num = num%11
        checknum = 11 - num

        #fill the '0' MSB
        if len(number)==10:
            if int(checknum) == int(number[9]):
                return True
        elif len(number)==9:
            if int(checknum) == int(number[8]):
                return True
        elif len(number)==8:
            if int(checknum) == int(number[7]):
                return True
        else:
            print("The Check Digit Provided Is Incorrect")
            return False
    except ValueError:
        print("Not Valid Number")

    except IndexError:
        print("Not 10 Digits")


def write_to_file(validated_isbn):
    with open( ISBN_LIST_FILE, 'w') as f:
        f.write(','.join(validated_isbn))
    f.close()

def open_isbn_file():
    """ Return list of ISBN strings """
    with open( ISBN_LIST_FILE, 'r') as f:
        line=f.readlines()
    list_of_isbn = line[0].split(",")
    return list_of_isbn

def generate_isbn_list_file():
    """write ISBNs to text file"""
    validated_isbn = []
    for START_ISBN, END_ISBN in ISBN_LIST:

        for i in range(START_ISBN, END_ISBN):
            if check_digit(i):
                validated_isbn.append(str(i))
            else:
                continue
        print(len(validated_isbn))
    write_to_file(validated_isbn)

    print("Num of ISBNs: "+str(len(validated_isbn)))


if __name__ == '__main__':
    generate_isbn_list_file()
