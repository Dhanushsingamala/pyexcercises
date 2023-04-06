class library:
    def __init__(self,books,no_of_books):
        self.books = books
        self.no_of_books = no_of_books
        
    def check(self):
        if self.no_of_books == len(self.books):
            return 1
        else:
            print("sorry invalid,no of books not equals to len of books")
            
    def append(self,new_book):
        self.books.append(new_book)
        
    def count(self):
        no_of_books = len(self.books)
        return no_of_books
    
    def showinfo(self):
        print(f'the no of books are {self.no_of_books} and the books are:')
        for book in self.books:
            print(book)
        
        
    
    
         
library1 = library(['ramayan','mahabarat','panchatantra'],3)       
h = library1.check()
print(h)
library1.append('python')
print(library1.books)
no_bk=library1.count()
print(no_bk)
library1.showinfo()

#such that we can also create differnt and n objects(libraries)