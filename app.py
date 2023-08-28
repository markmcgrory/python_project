from flask import Flask, render_template

from controllers.books_controller import books_blueprint
from controllers.wholesalers_controller import wholesalers_blueprint

app = Flask(__name__)

app.register_blueprint(books_blueprint)
app.register_blueprint(wholesalers_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET'])
def add():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(debug=True)