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
    new_book = Book(title=title, author=author, genre=genre)
    add_new_book(new_book)
    return redirect('/books')


@app.route('/books/<book_index>')
def individual_book(book_index):
    return render_template('book.html', title='Individual Book', book=book_list[int(book_index)])

@app.route('/books/delete/<book_title>', methods=['POST'])
def delete(book_title):
    delete_book(book_title)
    return redirect('/books')