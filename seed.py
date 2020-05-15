from binding import *

from pony.orm import *

from model.delivery_courier import DeliveryCourier
from model.delivery_shop import DeliveryShop
from model.pay_type import PayType
from model.product import Product
from model.product_type import ProductType
from model.shop import Shop

with db_session:
    try:
        product_type = ProductType(name="Верх")
        product_type1 = ProductType(name="Низ")

        product_type3 = ProductType(name="Тело", product_type=product_type)
        product_type4 = ProductType(name="Ноги", product_type=product_type1)

        product_type5 = ProductType(name="Футболки", product_type=product_type3)
        product_type7 = ProductType(name="Куртки", product_type=product_type3)
        product_type6 = ProductType(name="Кроссовки", product_type=product_type4)
        product_type8 = ProductType(name="Сапоги", product_type=product_type4)

        PayType(name="Наличными")
        PayType(name="По карте")

        shop = Shop(address="ул. Пушкина д. Колотушкина")
        Shop(address="ул. Ленина д. Коренина")

        # DeliveryShop(shop=shop)

        # DeliveryCourier(address="abvgd")

        # select(s for s in Shop).show()

        # 3 футболки
        Product(size=40, color="white", price=500, quantity=15, product_type=product_type5)
        Product(size=41, color="red", price=5001, quantity=151, product_type=product_type5)
        Product(size=42, color="black", price=5002, quantity=152, product_type=product_type5)

        # 2 куртки
        Product(size=40, color="orange", price=5001, quantity=152, product_type=product_type7)
        Product(size=41, color="pink", price=5002, quantity=153, product_type=product_type7)

        # 3 кросоовки

        Product(size=41, color="pink", price=5002, quantity=151, product_type=product_type6)
        Product(size=42, color="white", price=5001, quantity=154, product_type=product_type6)
        Product(size=43, color="red", price=5004, quantity=153, product_type=product_type6)

        # 2 сапоги

        Product(size=41, color="black", price=1333, quantity=151, product_type=product_type8)
        Product(size=41, color="brown", price=3221, quantity=10, product_type=product_type8)

    except Exception:
        pass
