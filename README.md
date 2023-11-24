<img width="1256" alt="Screenshot 2023-11-24 at 20 52 34" src="https://github.com/markmcgrory/python_project/assets/136241504/3e0cb149-63e5-410e-9f19-46caef49dc05">


### Initial CodeClan Brief: Shop Inventory

"Build an app which allows a shopkeeper to track their shop's inventory. This is not an app which the customer will see, it is an admin/management app for the shop workers." 

"Inspired by eBay, Amazon (back end only), Magento."

My approach was to build a "Bookshop Manager" web app aimed at staff working in a small bookstore. Functionality implemented: show book inventory, add to it or delete from it, show book details, update book details. Ditto with wholesalers, but the user can also filter books by wholesaler.

### Rules

"The project must be built using only:

HTML / CSS, Python, Flask, PostgreSQL and the psycopg."

<img width="1262" alt="Screenshot 2023-11-24 at 20 53 01" src="https://github.com/markmcgrory/python_project/assets/136241504/c9d5b53d-850f-4108-b9c1-4ee6384bf6fd">


## Setup & Installation
#### 1. Git clone the repo locally
```
#terminal
git clone git@github.com:markmcgrory/python_project.git
```
#### 2. Create the database
- Check whether PostgreSQL/PSYCOPG2 are installed on your computer
```
#terminal
psql
```
- If not installed, find the installation guide [here](https://www.psycopg.org/docs/install.html)

- Create database
```
#terminal
dropdb bookshop_manager
createdb bookshop_manager
```
- Initialise the tables for the database
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
- Make sure that nothing else is running on your localhost port 4999. If so, change the port on the .flaskenv file to a different one (like 5000)
- Start the app
```
#terminal
flask run
```
