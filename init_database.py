import os
from flask import Flask
from models.item import ItemModel
from db import db

from faker import Faker
from faker.providers import company, lorem


def load_initial_data():
    fake = Faker('ru_RU')
    fake.add_provider(lorem)
    fake.add_provider(company)

    for i in range(6):
        name = fake.word()
        price = fake.pyint()
        description = fake.text(max_nb_chars=300, ext_word_list=None)
        image_file = f"image_({i}).jpg"
        item = ItemModel(name, price, description, image_file)
        item.save_to_db()
        print(item)


init = Flask(__name__)
init.config['DEBUG'] = True
init.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')
init.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(init)
init.app_context().push()

if __name__ == '__main__':
    db.create_all()
    load_initial_data()
