from dto.basket_dto import BasketDTO
from dto.client_dto import ClientDTO
from dto.order_dto import OrderDTO
from dto.product_dto import ProductDTO
from model.basket import Basket
from seed import *

from dto.product_type_dto import ProductTypeDTO
from service.basket_service import BasketService
from service.client_service import ClientService
from service.delivery_courier_service import DeliveryCourierService
from service.delivery_shop_service import DeliveryShopService
from service.order_service import OrderService
from service.pay_type_service import PayTypeService
from service.product_service import ProductService
from service.product_type_service import ProductTypeService

# create product types
product_type_service = ProductTypeService()

types = product_type_service.get_all()

product_type_f = ProductTypeDTO(name="Кроссовки без шурков", product_type=types[5])
product_type_service.create(product_type_f)
print(product_type_f)

types = product_type_service.get_all()

for type in types:
    product_type_service.load_product_type(type)
    print(type)

# create client
client_dto = ClientDTO(name="user", login="user1337", password="123")
client_dto1 = ClientDTO(name="user1", login="user13371", password="1123")

client_cervice = ClientService()
client_cervice.create(client_dto)
client_cervice.create(client_dto1)

clients = client_cervice.get_all()

for client in client_cervice.get_all():
    print(client)

# create products

product_dto1 = ProductDTO(size=10, color="red", price=10, quantity=54, product_type=types[6])
product_dto2 = ProductDTO(size=101, color="red1", price=101, quantity=541, product_type=types[4])

product_service = ProductService()

product_service.create(product_dto1)
product_service.create(product_dto2)

products = product_service.get_all()
for product in products:
    product_service.load_product_type(product)
    print(product)

# create order
delivery_shop_service = DeliveryShopService()
delivery_courier_service = DeliveryCourierService()

delivery_shops = delivery_shop_service.get_all()
delivery_couriers = delivery_courier_service.get_all()

pay_type_service = PayTypeService()
pay_types = pay_type_service.get_all()

# create basket
basket_dto = BasketDTO()
basket_dto.add_product(products[0])
basket_service = BasketService()
basket_service.create(basket_dto)

'''
b = select(bb for bb in Basket)[:]
for bb in b:
    print(bb.products)
'''

baskets = basket_service.get_all()

# НЕ показывает товары в корзине!!!!
for basket in baskets:
    basket_service.load_products(basket)
    print(basket)

#ПОКАЗЫВАЕТ НЕ ТОТ DELIVERY!!!
order_dto = OrderDTO(payed=True, client=clients[0], pay_type=pay_types[0], delivery=delivery_shops[0],basket=baskets[0])
order_service = OrderService()
order_service.create(order_dto)
delivery_shop_service.load_shop(order_dto.delivery)
print(order_dto)
