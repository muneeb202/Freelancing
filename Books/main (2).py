import csv

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("\nEnter a number")


def validate_number(books, isbn):
    if len(isbn) != 17:
        return False
    if isbn[0:3] != "978" and isbn[0:3] != "979":
        return False
    for book in books:
        if book[0] == isbn:
            print("\nBook Already Exists")
            return False
    return True


def add_book(books):
    isbn = input("\nEnter ISBN : ")
    count = 0
    cost = 0.00
    sell = 0.00

    while not validate_number(books, isbn):
        print("\nInvalid ISBN Number !!!\n")
        isbn = input("Enter ISBN : ")

    name = input("Enter Name : ")

    while True:
        count = int(get_number("Enter Number of copies : "))
        if 1 <= count <= 10:
            break
        print("\nEnter a number between 1 and 10 !!\n")

    while True:
        cost = get_number("Enter Cost : ")
        if 1 <= cost <= 100:
            break
        print("\nEnter a number between 1.00 and 100.00 !!\n")

    while True:
        sell = get_number("Enter Selling price : ")
        if 2 <= sell <= 180 and sell > cost:
            break
        elif sell <= cost:
            print("\nSelling price should be greater than the cost !!\n")
        else:
            print("\nEnter a number between 1.00 and 180.00 !!\n")

    books.append([isbn, name, count, cost, sell])


def list_books(books):
    if len(books) == 0:
        print("\nLibrary Is Empty !!!")
    curr = 1
    for row in books:
        print("\n --------------  Book # " + str(curr) + "  --------------")
        print(" ISBN \t\t\t\t: \t\t" + row[0])
        print(" Author Name \t\t: \t\t" + row[1])
        print(" Copies \t\t\t: \t\t" + str(row[2]))
        print(" Cost Price \t\t: \t\t" + "%.2f" % (row[3]))
        print(" Selling Price \t\t: \t\t" + "%.2f" % (row[4]))
        print(" Profit\t\t\t\t:\t\t" + "%.2f" % (row[4] - row[3]) + "\n")
        curr += 1


def view_book_details(books, isbn):
    for book in books:
        if book[0] == isbn:
            print("\n ISBN \t\t\t\t: \t\t" + book[0])
            print(" Author Name \t\t: \t\t" + book[1])
            print(" Copies \t\t\t: \t\t" + str(book[2]))
            print(" Cost Price \t\t: \t\t" + "%.2f" % (book[3]))
            print(" Selling Price \t\t: \t\t" + "%.2f" % (book[4]))
            print(" Profit\t\t\t\t:\t\t" + "%.2f" % (book[4] - book[3]) + "\n")
            break
    else:
        print("\nNo Book with ISBN " + isbn + " exists !!\n")


def search_author(books, author):
    check = False
    for book in books:
        if book[1].lower() == author.lower():
            print("\n ISBN \t\t\t\t: \t\t" + book[0])
            print(" Author Name \t\t: \t\t" + book[1])
            print(" Copies \t\t\t: \t\t" + str(book[2]))
            print(" Cost Price \t\t: \t\t" + "%.2f" % (book[3]))
            print(" Selling Price \t\t: \t\t" + "%.2f" % (book[4]))
            print(" Profit\t\t\t\t:\t\t" + "%.2f" % (book[4] - book[3]) + "\n")
            check = True
    if not check:
        print("\nNo Book with Author " + author + " exists !!\n")


def update_stock(books, isbn):
    for book in books:

        if book[0] == isbn:
            while True:
                opt = input("\nEnter d to decrease stock, i to increase stock : ")
                if opt.lower() == 'd' or opt.lower() == 'i':
                    break
                print("\nInvalid Input !! Enter Again")

            print("\nCurrent Number of Copies of Book : " + str(book[2]))
            value = int(get_number("\nEnter Value : "))
            if opt.lower() == 'd':
                value = value * -1

            if book[2] + value > 10:
                print("\nNumber of copies cannot be greater than 10 !!\n")
            elif book[2] + value < 0:
                print("\nNumber of copies cannot be lesser than 0 !!\n")
            else:
                book[2] += value
                print("\nStock has been updated !!!")
            break
    else:
        print("\nNo Book with ISBN " + isbn + " exists !!\n")


def total_stock_value(books):
    total_cost = 0.0
    total_sell = 0.0

    for book in books:
        total_cost += book[3]
        total_sell += book[4]

    print("\nTotal Stock Cost : " + "%.2f" % total_cost
          + "\nTotal Profit : " + "%.2f" % (total_sell - total_cost) + "\n")


def menu():
    print("\n\t\t\t\t1 : Add a book"
          "\n\t\t\t\t2 : List all books"
          "\n\t\t\t\t3 : Display a book's details"
          "\n\tMenu\t\t4 : Search an author"
          "\n\t\t\t\t5 : Update stock"
          "\n\t\t\t\t6 : Total stock value"
          "\n\t\t\t\t7 : Exit")

    while True:
        try:
            inp = int(input("\nEnter Option : "))
            if 1 <= inp <= 7:
                return inp
            print("\nEnter a valid option !!!")
        except ValueError:
            print("\nEnter a number !!!")


def output_file(books):

    try:
        with open("books.csv", 'w') as csvfile:
            write = csv.writer(csvfile)
            write.writerow(["ISBN", "Author", "Copies", "Cost", "Selling Price"])
            write.writerows(books)
            print("\nLibrary written to file books.csv !!!")

    except IOError as e:
        print("\nKindly Close books.csv File !!!\n")
        input("\nPress Enter To Try Again !")
        output_file(books)


def main():
    book_list = []

    while True:
        opt = menu()

        if opt == 1:
            add_book(book_list)
        elif opt == 2:
            list_books(book_list)
        elif opt == 3:
            view_book_details(book_list, input("\nEnter ISBN : "))
        elif opt == 4:
            search_author(book_list, input("\nEnter Author Name : "))
        elif opt == 5:
            update_stock(book_list, input("\nEnter ISBN : "))
        elif opt == 6:
            total_stock_value(book_list)
        elif opt == 7:
            break

    output_file(book_list)


if __name__ == "__main__":
    main()
