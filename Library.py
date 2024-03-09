class Library:
    def __init__(self,list_of_books,library_name):
        self.book = list_of_books
        self.name = library_name
        self.lend_dict = {}

    def display_book(self):
        print(f"Following books are available in {self.name}:")
        for book in self.book:
            print(book)

    def lend_book(self,user,book):
        if book not in self.lend_dict.keys():
            self.lend_dict.update({book:user})
            print("Database has been succesfully updated. You can take a book now")
        else:
            print(f"{self.lend_dict[book]} is already taken ")

    def add_book(self,new_book):
        self.book.append(new_book)
        print("Book has been Succesfully added to the book list")

    def return_book(self,book):
        self.lend_dict.pop(book)
        print("You book has been successfully returned")

if __name__ == '__main__':
    SKN_Libaray=Library(['Python', 'Rich Daddy Poor Daddy', 'Harry Poter','C++ Basic'], 'Mahesh_Library')
    print("*"*75)
    print("""             1. Display All Books
             2. Lend a Book
             3. Add New Book
             4. Return a Book   """)
    print("*"*75)  
    while(True):
        choise = input("Enter a choise to perfrom a Operation: ")
        if choise == '1':
            SKN_Libaray.display_book()
        elif choise == '2':
            user = input("Enter Your Name: ")
            book = input("Enter book name to lend: ")
            SKN_Libaray.lend_book(user,book)
        elif choise == '3':
            book = input("Enter a book name to add: ")
            SKN_Libaray.add_book(book)
        elif choise == '4':
            book = input("Enter a book to return: ")
            SKN_Libaray.return_book(book)
        else:
            print("Please enter a valid option.")

        print(" Press q to Quit and c to Continue: ")
        user_choise = input()
        while(user_choise != "c" and user_choise != "q"):
            if user_choise == "q":
                exit()
            elif user_choise == "c":
                continue
            else:
                print("Enter a Valid Option") 