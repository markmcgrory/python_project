### Initial CodeClan Brief: Shop Inventory

"Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers." 

"Inspired by eBay, Amazon (back end only), Magento."

My approach was to build a "Bookshop Manager" web app aimed at staff working in a small bookstore. Functionality implemented: show book inventory, add to it or delete from it, show book details, update book details. Ditto with wholesalers, but the user can also filter books by wholesaler.

### Rules

"The project must be built using only:

HTML / CSS, Python, Flask, PostgreSQL and the psycopg."

## Setup & Installation
#### 1. Git clone the repo on local machine
```
#terminal
git clone git@github.com:markmcgrory/python_project.git
```
#### 2. Create the database
- Check wether PostgreSQL/PSYCOPG2 are installed on the machine
```
#terminal
psql
```
- If not installed, find the installation guide [here](https://www.psycopg.org/docs/install.html)
- Create database
```
#terminal
createdb bookshop_manager
```
- initializing the tables for the database
```
#terminal
psql -d bookshop_manager -f db/bookshop_manager.sql
```
#### 3. Initialize the database
- populate the database with dummy data
```
#terminal (cd in the root folder)
python3 console.py
```
#### 4. Starting the app
- make sure that nothing else is running on your localhost port 4999. If so, change the port on the .flaskenv file to a different one (like 5000)
- start the app
```
#terminal
flask run
```
