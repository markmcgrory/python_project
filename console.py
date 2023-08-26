import pdb
from models.book import Book
from models.wholesaler import Wholesaler

import repositories.book_repository as book_repository
import repositories.wholesaler_repository as wholesaler_repository

book_repository.delete_all()
wholesaler_repository.delete_all()

wholesaler1 = Wholesaler("Lomond Books", "Geoff", "07905487281", "geoff@lomondbooks.co.uk")
wholesaler_repository.save(wholesaler1)
wholesaler2 = Wholesaler("Alba Books", "Jane", "07584937557", "jane@lomondbooks.com")
wholesaler_repository.save(wholesaler2)
wholesaler3 = Wholesaler("Books For You", "Tunde", "07558833928", "info@booksforyou.org")
wholesaler_repository.save(wholesaler3)

book1 = Book("Street Cafe Vietnam", "Annabel Jackson", "Cookbook", "Conran Octopus Ltd", 1998, 7, 5.99, 7.99, wholesaler1)
book_repository.save(book1)
book2 = Book("Walden", "Henry David Thoreau", "Memoir", "Everyman's Library", 1910, 2, 8.50, 10, wholesaler2)
book_repository.save(book2)
book3 = Book("On the Road", "Jack Kerouac", "Fiction", "Penguin Books", 1957, 12, 4.99, 6.99, wholesaler2)
book_repository.save(book3)
book4 = Book("The Shipping News", "E.Annie Proulx", "Fiction", "Fourth Estate", 1993, 1, 2.99, 5.00, wholesaler2)
book_repository.save(book4)
book5 = Book("The Rough Guide to Film", "Richard Armstrong", "Nonfiction", "Rough Guides", 2007, 15, 9.99, 10.99, wholesaler1)
book_repository.save(book5)
book6 = Book("Blue River, Black Sea", "Andrew Eames", "Nonfiction", "Black Swan", 2009, 5, 4.14, 5.00, wholesaler3)
book_repository.save(book6)
book7 = Book("I Am Pilgrim", "Terry Hayes", "Fiction", "Corgi", 2013, 7, 4.50, 6.99, wholesaler2)
book_repository.save(book7)
book8 = Book("The Enemy", "Lee Child", "Fiction", "Bantam Books", 2004, "3", 2.79, 5.99, wholesaler2)
book_repository.save(book8)
book9 = Book("No Middle Name", "Lee Child", "Fiction", "Bantam Books", 2017, 4, 2.79, 5.99, wholesaler2)
book_repository.save(book9)
book10 = Book("Fresh-Air Fiend", "Paul Theroux", "Nonfiction", "Penguin Books", 2001, 2, 4.50, 7.99, wholesaler3)
book_repository.save(book10)



