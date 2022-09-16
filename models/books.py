import datetime
from models.book_class import Book

book_1 = Book('The Grapes of Wrath', 'John Steinbeck', 'Historical Fiction', False)
book_2 = Book('A Game of Thrones', 'G.R.R. Martin', 'Fantasy', True)
book_2.return_by = datetime.date(2023,1,25)
book_3 = Book('Total Recall', 'Arnold Schwarzenneger', 'Non-Fiction', False)

book_list = [book_1, book_2, book_3]

def add_new_book(book_object):
    book_list.append(book_object)

def delete_book(book_title):
    book_to_delete = None
    for book in book_list:
        if book_title == book.title:
            book_to_delete = book
            book_list.remove(book_to_delete)

def check_book_out(book_to_check_out, date):
    for book in book_list:
        if book.title == book_to_check_out:
            book.checked_out = True
            book.return_by = date