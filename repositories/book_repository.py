from db.run_sql import run_sql

from models.book import Book
from models.wholesaler import Wholesaler
import repositories.wholesaler_repository as wholesaler_repository


def save(book):
    sql = "INSERT INTO books (title, author, genre, publisher, publication_year, copies, cost_price, sell_price, wholesaler_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author, book.genre, book.publisher, book.publication_year, book.copies, book.cost_price, book.sell_price, book.wholesaler.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book


def select_all():
    books = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        wholesaler = wholesaler_repository.select(row['wholesaler_id'])
        book = Book(row['title'], row['author'], row['genre'], row['publisher'], row['publication_year'], row ['copies'], row['cost_price'], row['sell_price'], wholesaler, row ['id'])
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

def delete_all():
    sql = "DELETE  FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE  FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)
