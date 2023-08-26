from flask import Flask, render_template, request, redirect, Blueprint

from models.book import Book
import repositories.book_repository as book_repository

books_blueprint = Blueprint("books", __name__)