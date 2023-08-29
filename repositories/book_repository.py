from db.run_sql import run_sql

from models.book import Book
import repositories.wholesaler_repository as wholesaler_repository
import pdb

def save(book):
    sql = "INSERT INTO books (title, author, genre, publisher, publication_year, copies, cost_price, markup, wholesaler_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [book.title, book.author, book.genre, book.publisher, book.publication_year, book.copies, book.cost_price, book.markup, book.wholesaler.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    book.id = id
    return book

def select_all():
    books = []

    sql = "SELECT * FROM books ORDER BY author"
    results = run_sql(sql)

    for row in results:
        wholesaler = wholesaler_repository.select(row['wholesaler_id'])
        book = Book(row['title'], row['author'], row['genre'], row['publisher'], row['publication_year'], row ['copies'], row['cost_price'], row['markup'], wholesaler, row ['id'])
        books.append(book)
    return books


def select(id):
    book = None
    sql = "SELECT * FROM books WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        wholesaler = wholesaler_repository.select(result['wholesaler_id'])
        book = Book(result['title'], result['author'], result['genre'], result['publisher'], result['publication_year'], result['copies'], result['cost_price'], result['markup'], wholesaler, result['id'])
    return book

def delete_all():
    sql = "DELETE FROM books"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM books WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(book):
    # pdb.set_trace()
    sql = "UPDATE books SET (title, author, genre, publisher, publication_year, copies, cost_price, markup, wholesaler_id) = (%s, %s, %s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [book.title, book.author, book.genre, book.publisher, book.publication_year, book.copies, book.cost_price, book.markup, book.wholesaler.id, book.id]
    print(values)
    run_sql(sql, values)

def books_for_wholesaler(wholesaler):
    books = []

    sql = "SELECT * FROM books WHERE wholesaler_id = %s"
    values = [wholesaler.id]
    results = run_sql(sql, values)

    for row in results:
        book = Book(row['title'], row['author'], row['genre'], row['publisher'], row['publication_year'], row ['copies'], row['cost_price'], row['markup'], wholesaler, row ['id'])
        books.append(book)
    return books



