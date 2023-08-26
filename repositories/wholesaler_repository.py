from db.run_sql import run_sql

from models.wholesaler import Wholesaler
from models.book import Book


def save(wholesaler):
    sql = "INSERT INTO wholesalers (name, contact_person, contact_phone, contact_email) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [wholesaler.name, wholesaler.contact_person, wholesaler.contact_phone, wholesaler.contact_email]
    results = run_sql(sql, values)
    id = results[0]['id']
    wholesaler.id = id
    return wholesaler

def select(id):
    wholesaler = None
    sql = "SELECT * FROM wholesalers WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)

def delete_all():
    sql = "DELETE FROM wholesalers"
    run_sql(sql)


