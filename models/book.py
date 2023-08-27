class Book:
    
    def __init__ (self, title, author, genre, publisher, publication_year, copies, cost_price, markup, wholesaler, id = None):
        self.title = title
        self.author = author
        self.genre = genre
        self.publisher = publisher
        self.publication_year = publication_year
        self.copies = copies
        self.cost_price = cost_price
        self.markup = markup
        self.wholesaler = wholesaler
        self.id = id

    def calculate_sell_price(self):
        markup_amount = self.cost_price * (self.markup / 100)
        sell_price = self.cost_price + markup_amount
        return sell_price
    
        
        

