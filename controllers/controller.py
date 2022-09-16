from flask import render_template, request, redirect
from app import app
from models.books import *
from models.book_class import *

@app.route('/books')
def index():
    return render_template('index.html', title='Library - Home', book_list=book_list)

@app.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    new_book = Book(title=title, author=author, genre=genre, checked_out=False)
    add_new_book(new_book)
    return redirect('/books')


@app.route('/books/<book_index>')
def individual_book(book_index):
    return render_template('book.html', title=book_list[int(book_index)].title, book=book_list[int(book_index)])

@app.route('/books/delete/<book_title>', methods=['POST'])
def delete(book_title):
    delete_book(book_title)
    return redirect('/books')

@app.route('/books/checkout/<book_title>', methods=['POST'])
def check_out_book(book_title):
    return_date = request.form['date']
    book_to_check_out = book_title
    check_book_out(book_to_check_out, return_date)
    return redirect('/books')

@app.route('/books/checkin/<book_title>', methods=['POST'])
def check_in_book(book_title):
    book_to_check_in = book_title
    check_book_in(book_to_check_in)
    return redirect('/books')
