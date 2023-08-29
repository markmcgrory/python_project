from db.run_sql import run_sql

from models.wholesaler import Wholesaler
from models.book import Book
import repositories.wholesaler_repository as wholesaler_repository


def save(wholesaler):
    sql = "INSERT INTO wholesalers (name, contact_person, contact_phone, contact_email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [wholesaler.name, wholesaler.contact_person, wholesaler.contact_phone, wholesaler.contact_email]
    results = run_sql(sql, values)
    id = results[0]['id']
    wholesaler.id = id
    return wholesaler

def select_all():
    wholesalers = []

    sql = "SELECT * FROM wholesalers ORDER BY name"
    results = run_sql(sql)

    for row in results:
        wholesaler = Wholesaler(row['name'], row['contact_person'], row['contact_phone'], row['contact_email'], row['id'])
        wholesalers.append(wholesaler)
    return wholesalers

def select(id):
    wholesaler = None
    sql = "SELECT * FROM wholesalers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    if results:
        result = results[0]
        wholesaler = Wholesaler(result['name'], result['contact_person'], result['contact_phone'], result['contact_email'], result['id'])
    return wholesaler

def delete(id):
    sql = "DELETE FROM wholesalers WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM wholesalers"
    run_sql(sql)

def update(wholesaler):
    sql = "UPDATE wholesalers SET (name, contact_person, contact_phone, contact_email) = (%s, %s, %s, %s) WHERE id = %s"
    values = [wholesaler.name, wholesaler.contact_person, wholesaler.contact_phone, wholesaler.contact_email, wholesaler.id]
    print(values)
    run_sql(sql, values)




