from model.Delivery import Delivery
from model.DelivCourier import DelivCourier
from model.DelivShop import DelivShop
from model.ProductType import ProductType
from model.Product import Product
from model.Client import Client
from model.Shop import Shop
from model.Order import Order
from model.Basket import Basket
from model.PayType import PayType
from model.DataBase import db
from pony.orm import *

db.bind(provider='sqlite', filename='database.sqlite', create_db=True)
# set_sql_debug(True)

db.generate_mapping(create_tables=True)


with db_session:
    # Магазины
    shop1 = Shop(address="пл. Ломоносова, 1, Санкт-Петербург")
    shop2 = Shop(address="Приморское ш., д. 256А, Санкт-Петербург")

    # Типы товаров в магазине
    productTypeShoes = ProductType(name="Обувь")
    productTypeTShirt = ProductType(name="Футболка")

    productTypeSneakers = ProductType(name="Кроссовки", parent_type=productTypeShoes)
    productTypeBoots = ProductType(name="Ботинки", parent_type=productTypeShoes)

    productTypeTShirtMen = ProductType(name="Мужская футболка", parent_type=productTypeTShirt)
    productTypeTShirtWoman = ProductType(name="Женская футболка", parent_type=productTypeTShirt)

    # Продукты

    Sneakers = Product(size=42, color="Red", price=4500, quantity=10, product_type=productTypeSneakers)
    Sneakers1 = Product(size=44, color="Black", price=4500, quantity=10, product_type=productTypeSneakers)

    Boots = Product(size=40, color="Brown", price=5500, quantity=2, product_type=productTypeBoots)
    Boots1 = Product(size=45, color="Green", price=5500, quantity=2, product_type=productTypeBoots)

    MenTShirt = Product(size=40, color="Black", price=2000, quantity=40, product_type=productTypeTShirtMen)
    WomanTShirt = Product(size=30, color="White", price=2500, quantity=35, product_type=productTypeTShirtWoman)


