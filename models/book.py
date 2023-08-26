class Book:
    
    def __init__ (self, title, author, genre, publisher, publication_year, copies, cost_price, sell_price, wholesaler, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.publication_year = publication_year
        self.copies = copies
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.wholesaler = wholesaler
        self.id = id