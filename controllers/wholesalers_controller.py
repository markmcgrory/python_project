from flask import Blueprint, render_template, redirect, request
from models.wholesaler import Wholesaler
import repositories.wholesaler_repository as wholesaler_repository
import repositories.book_repository as book_repository

wholesalers_blueprint = Blueprint("wholesalers", __name__)

@wholesalers_blueprint.route("/wholesalers")
def wholesalers():
    wholesalers = wholesaler_repository.select_all()
    return render_template("wholesalers/index.html", wholesalers = wholesalers)

@wholesalers_blueprint.route("/wholesalers/new", methods=['GET'])
def new_wholesaler():
    return render_template("wholesalers/new.html")

@wholesalers_blueprint.route("/wholesalers/<id>", methods=['GET'])
def show_wholesaler(id):
    wholesaler = wholesaler_repository.select(id)
    return render_template('wholesalers/show.html', wholesaler=wholesaler)

@wholesalers_blueprint.route("/wholesalers", methods=['POST'])
def create_wholesaler():
    name = request.form['name']
    contact_person = request.form['contact_person']
    contact_phone = request.form['contact_phone']
    contact_email = request.form['contact_email']
    wholesaler = Wholesaler(name, contact_person, contact_phone, contact_email)
    wholesaler_repository.save(wholesaler)
    return redirect('/wholesalers')

@wholesalers_blueprint.route("/wholesalers/<id>/delete", methods=['POST'])
def delete_wholesaler(id):
    wholesaler_repository.delete(id)
    return redirect('/wholesalers')