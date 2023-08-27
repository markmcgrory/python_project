from flask import Blueprint, render_template, redirect, request
from models.wholesaler import Wholesaler
import repositories.wholesaler_repository as wholesaler_repository
import repositories.book_repository as book_repository

wholesalers_blueprint = Blueprint("wholesalers", __name__)

@wholesalers_blueprint.route("/wholesalers")
def wholesalers():
    wholesalers = wholesaler_repository.select_all()
    return render_template("wholesalers/index.html", wholesalers = wholesalers)

@wholesalers_blueprint.route("/wholesalers/<id>", methods=['GET'])
def show_wholesaler(id):
    wholesaler = wholesaler_repository.select(id)
    return render_template('wholesalers/show.html', wholesaler=wholesaler)

@wholesalers_blueprint.route("/wholesalers/<id>/delete", methods=['POST'])
def delete_wholesaler(id):
    wholesaler_repository.delete(id)
    return redirect('/wholesalers')