import pdb
from models.book import Book
from models.wholesaler import Wholesaler

import repositories.book_repository as book_repository
import repositories.wholesaler_repository as wholesaler_repository

book_repository.delete_all()
wholesaler_repository.delete_all()

wholesaler1 = Wholesaler("Lomond Books", "Geoff", "07905487281", "geoff@lomondbooks.co.uk")
wholesaler_repository.save(wholesaler1)
wholesaler2 = Wholesaler("Alba Books", "Jane", "07584937557", "jane@albabooks.com")
wholesaler_repository.save(wholesaler2)
wholesaler3 = Wholesaler("Books For You", "Tunde", "07558833928", "info@booksforyou.org")
wholesaler_repository.save(wholesaler3)

book1 = Book("Street Cafe Vietnam", "Jackson, Annabel", "Cookbook", "Conran Octopus Ltd", 1998, 7, 5.99, 20, wholesaler1)
book_repository.save(book1)
book2 = Book("Walden", "Thoreau, Henry David", "Memoir", "Everyman's Library", 1910, 2, 8.50, 20, wholesaler2)
book_repository.save(book2)
book3 = Book("On the Road", "Kerouac, Jack", "Fiction", "Penguin Books", 1957, 12, 4.99, 20, wholesaler2)
book_repository.save(book3)
book4 = Book("The Shipping News", "Proulx, E. Annie", "Fiction", "Fourth Estate", 1993, 1, 2.99, 30, wholesaler2)
book_repository.save(book4)
book5 = Book("The Rough Guide to Film", "Armstrong, Richard", "Nonfiction", "Rough Guides", 2007, 15, 9.99, 20, wholesaler1)
book_repository.save(book5)
book6 = Book("Blue River, Black Sea", "Eames, Andrew", "Nonfiction", "Black Swan", 2009, 5, 4.14, 30, wholesaler3)
book_repository.save(book6)
book7 = Book("I Am Pilgrim", "Hayes, Terry", "Fiction", "Corgi", 2013, 7, 4.50, 40, wholesaler2)
book_repository.save(book7)
book8 = Book("The Enemy", "Child, Lee", "Fiction", "Bantam Books", 2004, 3, 2.79, 20, wholesaler2)
book_repository.save(book8)
book9 = Book("No Middle Name", "Child, Lee", "Fiction", "Bantam Books", 2017, 4, 2.79, 30, wholesaler2)
book_repository.save(book9)
book10 = Book("Fresh-Air Fiend", "Theroux, Paul", "Nonfiction", "Penguin Books", 2001, 2, 4.50, 25, wholesaler3)
book_repository.save(book10)



pdb.set_trace()


