from flask import Flask, render_template, request, redirect, Blueprint

from models.book import Book
import repositories.book_repository as book_repository
import repositories.wholesaler_repository as wholesaler_repository

books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/books")
def books():
    books = book_repository.select_all()
    return render_template("books/index.html", books = books)


@books_blueprint.route("/books/new", methods=['GET'])
def new_book():
    wholesalers = wholesaler_repository.select_all()
    return render_template("books/new.html", wholesalers=wholesalers)

@books_blueprint.route("/books/<id>", methods=['GET'])
def show_book(id):
    book = book_repository.select(id)
    return render_template('books/show.html', book=book)

@books_blueprint.route("/books", methods=['POST'])
def create_book():
    title = request.form['title']
    author = request.form['author']
    genre = request.form['genre']
    publisher = request.form['publisher']
    publication_year = request.form['publication_year']
    copies = request.form['copies']
    cost_price = request.form['cost_price']
    markup = request.form['markup']
    wholesaler = wholesaler_repository.select(request.form['wholesaler_id'])
    book = Book(title, author, genre, publisher, publication_year, copies, cost_price, markup, wholesaler)
    book_repository.save(book)
    return redirect('/books')

@books_blueprint.route("/books/<id>/edit", methods=['GET'])
def edit_book(id):
    book = book_repository.select(id)
    wholesalers = wholesaler_repository.select_all()
    return render_template('books/edit.html', book=book, wholesalers=wholesalers)


