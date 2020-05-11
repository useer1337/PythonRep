from database import db
from model import basket, client, delivery, delivery_courier, delivery_shop, order, pay_type, product_type, product, shop

db.bind(provider='sqlite', filename='db_exmaple', create_db=True)
db.generate_mapping(create_tables=True)