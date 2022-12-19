from __init__ import db

class category(db.Model):
    category_id = db.Column(db.Integer(), primary_key = True, nullable=False)
    name = db.Column(db.String(), nullable = False)

class manufacturer(db.Model):
    manufacturer_id = db.Column(db.Integer(), primary_key = True, nullable=False)
    name = db.Column(db.String(), nullable = False)

class item(db.Model):
    item_id = db.Column(db.Integer(), primary_key = True, nullable = False)
    name = db.Column(db.String(), nullable = False)
    category_id = db.Column(db.Integer(), db.ForeignKey('category.category_id'))
    manufacturer_id = db.Column(db.Integer(), db.ForeignKey('manufacturer.manufacturer_id'))
    price = db.Column(db.Integer())


class buyer(db.Model):
    buyer_id = db.Column(db.Integer(), primary_key = True, nullable=False)
    name = db.Column(db.String(), nullable = False)

class shop_order(db.Model):
    shop_order_id = db.Column(db.Integer(), primary_key = True, nullable = False)
    buyer_id = db.Column(db.Integer(), db.ForeignKey('buyer.manufacturer_id'))



item_shop_order = db.Table('item_shop_order',
            db.Column('shop_order_id', db.Integer, db.ForeignKey('shop_order.shop_order_id')),
            db.Column('item_id', db.Integer, db.ForeignKey('item.item_id'))
            )