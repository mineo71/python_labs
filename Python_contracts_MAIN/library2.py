# Декоратор для логування
def log_action(action):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f"{action} - {args[0].__class__.__name__}.{func.__name__}")
            return result
        return wrapper
    return decorator

# Клас представлення книги
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

# Клас представлення бібліотекаря
class Librarian:
    @log_action("Adding book")
    def add_book(self, library, book):
        library.add_book(book)

    @log_action("Removing book")
    def remove_book(self, library, book):
        library.remove_book(book)

# Клас представлення бібліотеки
class Library:
    def __init__(self):
        self.books = []

    @log_action("Reading books from file")
    def read_books_from_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                title, author, isbn = line.strip().split(',')
                self.add_book(Book(title, author, isbn))

    @log_action("Writing books to file")
    def write_books_to_file(self, filename):
        with open(filename, 'w') as file:
            for book in self.books:
                file.write(f"{book.title},{book.author},{book.isbn}\n")

    @log_action("Adding book to library")
    def add_book(self, book):
        self.books.append(book)

    @log_action("Removing book from library")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)

    def display_books(self):
        for book in self.books:
            print(book)

# Приклад використання
library = Library()
librarian = Librarian()

# Додаємо книги до бібліотеки
librarian.add_book(library, Book("The Great Gatsby", "F. Scott Fitzgerald", "978-3-16-148410-0"))
librarian.add_book(library, Book("To Kill a Mockingbird", "Harper Lee", "978-0-06-112008-4"))
librarian.add_book(library, Book("1984", "George Orwell", "978-0-452-28423-4"))

# Видаляємо одну книгу
librarian.remove_book(library, library.books[0])

# Відображення книг в бібліотеці
print("Books in the library:")
library.display_books()

# Запис та читання книг з файлу
library.write_books_to_file("library_books.txt")
library.read_books_from_file("library_books.txt")
print("\nBooks after reading from file:")
library.display_books()
