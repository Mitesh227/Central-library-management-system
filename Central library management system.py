class Library:
    def __init__(self, listOfBooks):
        self.books = listOfBooks

    def displayAvailableBooks(self):
        print("Books present in this library are: ")
        for book in self.books: 
            print(" *" + book)
    
    def borrowBook(self, bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. Please keep it safe and return it within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry, This book is either not available or has already been issued to someone else. Please wait until the book is available")
            return False

    def returnBook(self, bookName):
        self.books.append(bookName)
        print("Thanks for returning this book! Hope you enjoyed reading it. Have a great day ahead!")

class Student: 
    def requestBook(self):
        self.book = input("Enter the name of the book you want to borrow: ")
        return self.book

    def returnBook(self):
        self.book = input("Enter the name of the book you want to return: ")
        if self.book==" " or self.bool=="  ":
            print("Invalid input")
        else:
            pass
        return self.book
         

if __name__ == "__main__":
    centraLibrary = Library(["How to Win Friends and Influence People By_Dale_Carnegie","Think and Grow Rich By_Napoleon_Hill","Laws of Success By_Napoleon_Hill","The 7 Habits of Highly Effective Teens By_Sean_Covey","As a Man Thinketh By_James_Allen","See You at the Top By_Zig_Ziglar","Rich Dad Poor Dad By_Robert_Kiyosaki","The 80/20 Principle By_Richard_Kosh","How to Get from Where You Are to Where You Want to Be By_Jack_Canfield","The Power Of Less By_Leo_Babauta","Brain Rules By_John_Medina","48 laws of power By_Robert_Greene","Mastery By_Robert_Greene"])
    student = Student()
    # centraLibrary.displayAvailableBooks()
    while(True):
        welcomeMsg = '''\n ====== Welcome to Central Library ======
        Please choose an option:
        1. List all the books
        2. Request a book
        3. Add/Return a book
        4. Exit the Library
        '''
        print(welcomeMsg)
        a = int(input("Enter a choice: "))
        if a == 1:
            centraLibrary.displayAvailableBooks()
        elif a == 2:
            centraLibrary.borrowBook(student.requestBook())
        elif a == 3:
            centraLibrary.returnBook(student.returnBook())
        elif a == 4:
            print("Thanks for choosing Central Library. Have a great day ahead!")
            exit()
        else:
            print("Invalid Choice!")

        
