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
        if book not in self.lend_dict:
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
    