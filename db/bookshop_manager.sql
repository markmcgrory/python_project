DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS wholesalers;

CREATE TABLE wholesalers (
    
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    contact_person VARCHAR(255),
    contact_phone VARCHAR (255),
    contact_email VARCHAR(255)
);

CREATE TABLE books(

    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255),
    genre VARCHAR(255),
    publisher VARCHAR(255),
    publication_year INT,
    copies INT,
    cost_price FLOAT,
    sell_price FLOAT,
    wholesaler_id INT NOT NULL REFERENCES wholesalers(id) ON DELETE CASCADE

);