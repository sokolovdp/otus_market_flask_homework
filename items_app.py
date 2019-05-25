from flask import Blueprint, render_template

from models.item import ItemModel

items_app = Blueprint('items_app', __name__)


@items_app.route('/')
def view_all_items():
    items = ItemModel.get_all_items()
    return render_template('list.html', items=items)


@items_app.route('/<int:item_id>')
def view_item(item_id):
    item = ItemModel.find_by_id(item_id)
    return render_template('detail.html', item=item)
