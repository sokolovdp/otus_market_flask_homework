import os
from flask import Flask, render_template
from items_app import items_app
from db import db

app = Flask(__name__)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.register_blueprint(items_app, url_prefix='/items')


@app.route('/')
def view_home():
    return render_template('home.html')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=8000)
