#!/usr/local/bin/python3

# CSE 231::730 Project 6

# Defining functions

def search_by_year_range(lst, y1, y2):
    print("All titles from year {0} to {1}".format(y1,y2))
    print('\n')
    for book in lst:
        for i in range(y1,y2):
            if int(book[3][2]) == i:
                myprint(book)
    
def search_by_date(lst,m,y):
    print("All titles in month {0} of {1}".format(m,y))
    print('\n')
    for book in lst:
        if (int(book[3][2]) == y) and (int(book[3][0]) == m)):
            myprint(book)
            

def search_for_author(lst, a):
    print("All books with author including character(s) {0}".format(a))
    print('\n')
    for book in lst:
        if a.upper() in book[1].upper():
            myprint(book)
    
def search_for_title(lst, t):
    print("All books with Title including character(s) {0}".format(t))
    print('\n')
    for book in lst:
        if t.upper() in book[0].upper():
            myprint(book)
    
def myprint(book):
    if book:
        print(book[0] + ", by " + book[1] + " (" + "/".join(book[3]) + ")")
    else:
        print("None")
    
def main(lst):
    
    while True:
        print("What would you like to do?")
        print("1: Lookup year range")
        print("2: Lookup month/year")
        print("3: Search for author")
        print("4: Search for title")
        print("Q: Quit")
        goo = input("> ")
        
        if (goo not in "1234qQ") or len(goo)>1:
            print("Bad Command Try again")
        else:
            if goo == "1":
                y1 = input("Enter Starting Year: ")
                y2 = input("Enter Ending Year: ")
                if y1.isdigit() and y2.isdigit() and int(y2)>int(y1):
                    search_by_year_range(lst, int(y1), int(y2))
                else:
                    print("Bad Input")
                    continue
            if goo == "2":
                month = input("Enter month (1-12): ")
                year = input("Enter year: ")
                if month.isdigit() and year.isdigit() and (int(month)>0) and (int(month)<13) and int(year)>0:
                    search_by_date(lst, int(month), int(year))
                else:
                    print("Bad Input")
                    continue
            if goo == "3":
                author = input("Enter author name (or part of name): ")
                search_for_author(lst, author)
            if goo == "4":
                title = input("Enter title name (or part of name): ")
                search_for_title(lst, title)
            if (goo == "Q") or (goo == "q"):
                print("Quitting...")
                break


# Importing file

f = open("bestsellers.txt", 'r+')

my_list = []

for line in f:
    book = line.strip().split('\t')
    book[3] = book[3].split("/")
    my_list.append(book)

f.close()


# Main call

main(my_list)
