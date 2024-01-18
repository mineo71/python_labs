# Система управлiння бiблiотекою
# Напишiть програму на Python, яка iмiтує систему управлiння бiблiотекою 
# з використанням об'єктно-орiєнтованого програмування (ООП), умовних конструкцi
# (if, else), та обробки файлiв. Ваша програма повинна мiстити:
# 1. Клас Book iз полями title (назва), author (автор), i year_published (рiк видання), 
# та методом для виводу iнформацiї про книгу. 2. Клас Library, який має список книг (books)
# та методи для додавання книг(book), пошуку книги за автором чи назвою (find_book), 
# та виводу всiх книг у форматi CSV у файлі library.csv. Зазвичай, книжки додаються вручну,
# проте ви повинні iмплементувати методи для введення декiлькох книг ззовнi за допомогою CSV файлу,
# що повинен бути прочитаний та оброблений без використання бiблiотек. Всі умовні конструкції
# та виключення повинні бути належно оброблені.

import csv

class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published

    def display_info(self):
        print(f"Назва: {self.title}, Автор: {self.author}, Рік публікації: {self.year_published}")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def find_book(self, search_key, search_value):
        found_books = []
        for book in self.books:
            if search_key == 'author' and book.author == search_value:
                found_books.append(book)
            elif search_key == 'title' and book.title == search_value:
                found_books.append(book)
        return found_books

    def display_all_books(self):
        for book in self.books:
            book.display_info()

    def save_to_csv(self):
        with open('library.csv', 'w', newline='') as csvfile:
            fieldnames = ['Назва', 'Автор', 'Рік публікації']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for book in self.books:
                writer.writerow({'Назва': book.title, 'Автор': book.author, 'Рік публікації': book.year_published})

    def load_from_csv(self):
        with open('library.csv', 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_book = Book(row['Назва'], row['Автор'], int(row['Рік публікації']))
                self.add_book(new_book)

book1 = Book("Book1", "O.Rylsky", 2005)
book2 = Book("Book2", "I.Litvinov", 2005)
book3 = Book("Book3", "N.Folush", 2003)
book4 = Book("Book4", "M.Zhmud", 2005)

library = Library()

print("Книжки в бібліотеці:")
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
library.add_book(book4)

library.display_all_books()

found_books_by_author = library.find_book('author', 'O.Rylsky')
found_books_by_title = library.find_book('title', 'Book4')

print("\nКнижки які були знайдені по автору:")
for book in found_books_by_author:
    book.display_info()

print("\nКнижки які були знайдені по назві:")
for book in found_books_by_title:
    book.display_info()

library.load_from_csv()
print("\nВсі книжки:")
library.display_all_books()
library.save_to_csv()