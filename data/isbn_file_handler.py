

# create list of ISBNs in text file
# call each isbn, record hit and misses, written to csv

# store data iin mySQL

#First Run
#START_ISBN = 1250107814
#END_ISBN =   1250110014

#Second Run
#START_ISBN = 330508113 #first digit is actually a zero
#END_ISBN =   330608113

#THIRS RUN
#START_ISBN = 552167835
#END_ISBN =   552267835


#fourth run
#START_ISBN = 765350386
#END_ISBN =   765750386

#fifth run
START_ISBN = 739382696
END_ISBN =  739982696

#200

ISBN_LIST_FILE = 'isbn_list.txt'

#currently fixed for 9 digits
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
        if len(number)==10:
            num = int(number[0]) * 10 + int(number[1]) * 9 + int(number[2]) * 8 + int(number[3]) * 7 + int(number[4]) * 6 + int(number[5]) * 5 + int(number[6]) * 4 + int(number[7]) * 3 + int(number[8]) * 2
        else:
            num = int(number[0]) * 9 + int(number[1]) * 8 + int(number[2]) * 7 + int(number[3]) * 6 + int(number[4]) * 5 + int(number[5]) * 4 + int(number[6]) * 3 + int(number[7]) * 2

        num = num%11
        checknum = 11 - num

        if len(number)==10:
            if int(checknum) == int(number[9]):
                return True
        elif len(number)==9: # to cater to isbn that starts with one '0'
            if int(checknum) == int(number[8]):
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
    with open( ISBN_LIST_FILE, 'w') as f:
        f.write(','.join(validated_isbn))
    f.close()

def open_isbn_file():
    with open( ISBN_LIST_FILE, 'r') as f:
        line=f.readlines()
    list_of_isbn = line[0].split(",")
    return list_of_isbn

def generate_isbn_list():
    """write ISBNs to text file"""
    validated_isbn = []
    for i in range(START_ISBN, END_ISBN):
        if check_digit(i):
            validated_isbn.append(str(i))
        else:
            continue

    write_to_file(validated_isbn)




if __name__ == '__main__':
    generate_isbn_list()
    print(open_isbn_file())
