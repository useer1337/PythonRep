from binding import *

from pony.orm import *

from model.delivery_courier import DeliveryCourier
from model.delivery_shop import DeliveryShop
from model.pay_type import PayType
from model.product_type import ProductType
from model.shop import Shop

with db_session:
    try:
        product_type = ProductType(name="Верх")
        product_type1 = ProductType(name="Низ")

        product_type3 = ProductType(name="Тело", product_type=product_type)
        product_type4 = ProductType(name="Ноги", product_type=product_type1)

        product_type5 = ProductType(name="Футболка", product_type=product_type3)
        product_type6 = ProductType(name="Кроссовки", product_type=product_type4)


        PayType(name="Наличными")
        PayType(name="По карте")

        shop = Shop(address="abvgd")

        DeliveryShop(shop=shop)


        DeliveryCourier(address="hhhhhhhhhhhhhhhhhhh")

    except Exception:
        pass
