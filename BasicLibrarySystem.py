
class Book:
    def __init__(self,name:str,author:str,year:str) -> None:
        self.name = name
        self.author = author
        self.year = year

    def getName(self) -> str:
        return self.name
    
    def getAuthor(self) -> str:
        return self.author
    
    def getYear(self) -> str:
        return self.year
    
    def setName(self,name:str) -> None:
        self.name = name
    
    def setAuthor(self,author:str) -> None:
        self.author = author

    def setYear(self,year:str) -> None:
        self.year = year

    def __str__(self) -> None:
        print(f"Book Name: {self.name}\nAuthor: {self.author}\nYear: {self.year}")

class Library:
    def __init__(self) -> None:
        self.books = []
    
    def add_book(self,book:Book) -> None:
        for b in self.books:
            if b.getName() == book.getName() and b.getAuthor() == book.getAuthor() and b.getYear() == book.getYear():
                print(f"{book.getName()} already exists")
                return None
        if book.getName() == "" or book.getAuthor() == "" or book.getYear() == "":
            print("Book name, author or year can not be empty")
            return None 
        self.books.append(book)
        print(f"{book.getName()} Başarıyla Eklendi")
    
    def remove_book(self,book:Book) -> None:
        if book not in self.books:
            print("Book not found")
            return None
        self.books.remove(book)
        print(f"{book.getName()} Başarıyla Silindi")
    
    def search_by_name(self,name:str) -> Book:
        for book in self.books:
            if book.getName() == name:
                return book
        return None
    
    def search_by_author(self,author:str) -> list:
        tempBooks = []
        for book in self.books:
            if book.getAuthor() == author:
                tempBooks.append(book)
        if len(tempBooks) == 0:
            return None
        return tempBooks
    
    def list_books(self) -> None:
        for book in self.books:
            print(f"Book Name: {book.getName()}\nAuthor: {book.getAuthor()}\nYear: {book.getYear()}")

#Testler
def autoTests(library:Library):
    #Book Nesnesi Oluşturma Testi
    book1 = Book("Book1","Author1","1999")
    book2 = Book("Book2","Author1","2002")
    book3 = Book("Book3","Author2","2000")
    book4 = Book("Book4","Author3","2001")
    book5 = Book("","","1987")
    book6 = Book("Book6","","")
    book7 = Book("","Author7","")
    book8 = Book("","Author8","1988")

    #Kitap Ekleme Testi
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book2) # 2. kez book2 eklenmeye çalışıldığında "Book2 already exists" mesajı verilir.
    library.add_book(book3)
    library.add_book(book4)
    library.add_book(book5) # Book name, author or year can not be empty mesajı verilir.
    library.add_book(book6) # Book name, author or year can not be empty mesajı verilir.
    library.add_book(book7) # Book name, author or year can not be empty mesajı verilir.
    library.add_book(book8) # Book name, author or year can not be empty mesajı verilir.

    #Kitap Listeleme Testi
    print("Books in Library:")
    print()
    library.list_books()
    print("------------------------------------------------")
    print("Search by Name: Book1")
    
    #İsme Göre Kitap Arama Testi
    book = library.search_by_name("Book1")
    print(f"Book Name: {book.getName()}\nAuthor: {book.getAuthor()}\nYear: {book.getYear()}")
    print("------------------------------------------------")
    print("Search by Author: Author1")
    
    #Yazara Göre Kitap Arama Testi
    books = library.search_by_author("Author1")
    for b in books:
        print(f"Book Name: {b.getName()}\nAuthor: {b.getAuthor()}\nYear: {b.getYear()}")
    print("------------------------------------------------")

    #Kitap Silme Testi
    print("Remove Book: Book1")
    library.remove_book(book1)
    print("------------------------------------------------")

    #Kitap Listeleme Testi
    print("Books in Library:")
    library.list_books()
    print("------------------------------------------------")

def manuelTest(library:Library):
    try:
        while True:
            print("--------------------Library---------------------")
            print("1- Add Book\n2- Remove Book\n3- Search by Name\n4- Search by Author\n5- List Books\n6- Exit")
            print("------------------------------------------------")
            choice = int(input("Enter your choice: "))

            #Kitap Ekleme
            if choice == 1:
                name = input("Enter Book Name: ")
                if len(name) == 0:
                    print("Book name can not be empty")
                    continue

                author = input("Enter Author: ")
                if len(author) == 0:
                    print("Author name can not be empty")
                    continue

                year = input("Enter Year: ")
                if len(year) == 0:
                    print("Year can not be empty")
                    continue
                if not year.isdigit():
                    print("Year must be a number")
                    continue
                if len(year) > 4:
                    print("Invalid Year")
                    continue

                book = Book(name,author,year)
                library.add_book(book)
                
            #Kitap Silme
            elif choice == 2:
                name = input("Enter Book Name: ")
                book = library.search_by_name(name)
                if book == None:
                    print("Book not found")
                    continue
                library.remove_book(book)
                
            #İsme Göre Kitap Arama
            elif choice == 3:
                name = input("Enter Book Name: ")
                book = library.search_by_name(name)
                if book == None:
                    print("Book not found")
                    continue
                print(f"Book Name: {book.getName()}\nAuthor: {book.getAuthor()}\nYear: {book.getYear()}")

            #Yazara Göre Kitap Arama
            elif choice == 4:
                author = input("Enter Author: ")
                books = library.search_by_author(author)
                if books == None:
                    print("Book not found")
                    continue
                for b in books:
                    print(f"Book Name: {b.getName()}\nAuthor: {b.getAuthor()}\nYear: {b.getYear()}")

            #Kitapları Listeleme
            elif choice == 5:
                print("Books in Library:")
                print("------------------------------------------------")
                library.list_books()
                if len(library.books) == 0:
                    print("No books in library")
                print("------------------------------------------------")

            #Çıkış
            elif choice == 6:
                break

            #Hatalı Giriş
            else:
                print("Invalid Choice")

    except:
        print("Invalid Input")


#Main
def main():
    library = Library() #Kütüphane nesnesi

    try:
        while True:
            testChoice = input("1- Manuel Test\n2- Auto Test\n3- Exit\nEnter your choice: ")
            
            if testChoice == "1":
                manuelTest(library)
                continue

            elif testChoice == "2":
                autoTests(library)
                continue

            elif testChoice == "3":
                break

            else:
                print("Invalid Choice")
    except:
        print("Invalid Input")


if __name__ == "__main__":
    main()