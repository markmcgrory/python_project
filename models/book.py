class Book:
    
    def __init__ (self, title, author, genre, publisher, copies, cost_price, sell_price, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.copies = copies
        self.cost_price = cost_price
        self.sell_price = sell_price
        self.id = id