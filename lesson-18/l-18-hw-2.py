class Book:
    def __init__(self, title, author=None, year=None) -> None:
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        if self.author and self.year:
            print('{:<30}{:<20}{:>5}'.format(
                self.title, self.author, self.year))
        elif self.author:
            print('{:<30}{:<20}{:>5}'.format(self.title, self.author, ''))
        elif self.year:
            print('{:<30}{:<20}{:>5}'.format(self.title, '', self.year))


# book_1 = Book('Hobbit', author='J.R.Tolkien', year=1937)
# book_2 = Book('Lord of the rings', author='J.R.Tolkien', year=1954)
# book_3 = Book('Dune', author='Frank Herbert', year=1937)

book_1 = Book('Чистый код', 'Дядя Боб', 2017)
book_2 = Book('От 2 до 5', 'Корней Чуковский', 1958)
book_3 = Book('Идеальный программист', 'Дядя Боб', 2018)
book_4 = Book('Рецепты татарской кухни', year=2018)


# book_1.display()


class Library:
    def __init__(self, title) -> None:
        self.name = title

        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list(self):
        print('{:<30}{:<20}{:>5}'.format('Название', 'Автор', 'Год'))
        for i in self.books:
            i.display()

    def filter(self, title=None, author=None, year=None):
        array = []
        for book in self.books:
            if book.author == author or book.title == title or book.year == year:
                array.append(book)
        return array

    @staticmethod
    def as_table(books):
        print('{:<30}{:<20}{:>5}'.format('Название', 'Автор', 'Год'))
        for book in books:
            book.display()


library = Library('Home library')

# print(library.name)

library.add_book(book_1)
library.add_book(book_2)
library.add_book(book_3)
library.add_book(book_4)

# library.list()

# books = library.filter(author='Корней Чуковский', title='От 2 до 5')
# books[0].display()

# books = library.filter(title='Hobbit', author='J.R.Tolkien', year=1937)
# books[0].display()
# books[1].display()
# print(books)

books = library.filter(author='Дядя Боб')
Library.as_table(books)  # вызов от имени класса
