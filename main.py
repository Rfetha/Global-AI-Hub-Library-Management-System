import os

class Library:
    def __init__(self, filename="books.txt"):
        self.filename = filename
        self.books = []
        self.load_books()

    def load_books(self):
        try:
            with open(self.filename, "r+") as file:
                if not file.read():
                    file.seek(0)
                for line in file:
                    book_info = line.strip. split(",")
        except FileNotFoundError:
            print("FileNotFoundError !!!")

    def save_books(self):
            with open(self.filename, "w") as file:
                for book in self.books:
                    file.write(",".join([
                        book["title"], book["author"],
                        str(book["release_year"]), str(book["pages"])
                    ]) + "\n")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("\n** List of Books **")
        for i, book in enu  merate(self.books):
            print(f"{i+1}.   {book['title']} by {book['author']} ({book['release_year']}, {book['pages']} pages)")

    def add_book(self): 
        title = input("Ent  er book title: ")
        author = input("En  ter author name: ")
        release_year = int  (input("Enter release year: "))
        pages = int(input(  "Enter number of pages: "))
        new_book = {
            "title": title  ,
            "author": auth  or,
            "release_year"  : release_year,
            "pages": pages  
        }
        self.books.append(  new_book)
        self.save_books()   
        print(f"Book '{tit  le}' by {author} added successfully!")

    def remove_book(self):  
        title = input("Ent  er title of book to remove: ")
        for i, book in enu  merate(self.books):
            if book["title  "].lower() == title.lower():
                self.books  .pop(i)
                self.save_  books()
                print(f"Bo  ok '{title}' removed successfully!")
                return  
        print(f"Book '{title}' not found.")

def main():
    lib = Library()

    while True:
        print("\n*** Library Management System ***")
        print("1. List Books")
        print("2. Add Book")
        print("3. Remove Book")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            lib.list_books()
        elif choice == "2":
            lib.add_book()
        elif choice == "3":
            lib.remove_book()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
        
        








































