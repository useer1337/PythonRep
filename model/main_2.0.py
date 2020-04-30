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

db.bind(provider='sqlite', filename='database.sqlite', create_db=False)
# set_sql_debug(True)

db.generate_mapping(create_tables=True)

with db_session:
    # Создание клиента
    select(c for c in Client).show()

    while True:
        verification = input("Зарегестрироваться/Войти в аккаунт(1/2) ")
        if verification == "1":
            name = input("Введите имя: ").strip()
            login = input("Введите логин: ").strip()
            password = input("Введите пароль: ").strip()

            if Client.get(login=login):
                print("Такой уже есть!!")
                continue

            client = Client(name=name, login=login, password=password)
            break
        else:
            name = input("Введите своё имя: ").strip()
            login = input("Введите свой логин: ").strip()
            password = input("Введите свой пароль: ").strip()
            client = Client.get(name=name, login=login, password=password)
            if client:
                break

        print("Вы ввели не правильные данные!!")

    # Заказ
    print("Оформление товара \n")
    basket = Basket()
    order = Order(client=client, basket=basket)

    while True:
        end = input("1) Заказать еще\n2) Посмотреть корзину\n3) Удалить товар из корзины\n4) Закончить выбирать "
                    "товары\n")

        if end == "1":

            product_types = select(p for p in ProductType if p.parent_type is None)[:]
            for product_type in product_types:
                print(product_type.get_nameType())

            choice = int(input("Выберите тип товара который у нас есть:\n"))

            product_types2 = select(p for p in ProductType if p.parent_type is product_types[choice - 1])[:]
            for product_type in product_types2:
                print(product_type.get_nameType())

            choice = int(input("Выберите тип товара который у нас есть:\n"))

            product_list = select(p for p in Product if p.product_type is product_types2[choice - 1])[:]

            for product in product_list:
                print("Цвет- " + product.get_color() + " размер- " + str(product.get_size()) + " цена- " + str(
                    product.get_price()))

            choice = int(input("Выберите товар который у нас есть:\n"))

            basket.add_product(product_list[choice - 1])

            continue

        elif end == "2":
            print("\n\tВаша корзина:\n")

            for product in order.get_basket().get_products():
                print('\t' + "Цвет- " + product.get_color() + " размер- " + str(product.get_size()) + " цена- " + str(
                    product.get_price()))

            continue

        elif end == "3":

            print("\n\tВаша корзина:\n")

            products_list = select(p for p in order.get_basket().get_products())[:]

            for product in products_list:
                print('\t' + "Цвет- " + product.get_color() + " размер- " + str(product.get_size()) + " цена- " + str(
                    product.get_price()))

            choice = int(input("Выерите номер товара кторый нужно удалить:\n"))

            order.get_basket().get_products().remove(products_list[choice-1])

            continue

        elif end == "4":
            break

        elif end == "5":
            order_list = select(o for o in client.order)[:]
            for observable_order in order_list[:-1]:
                print(str(observable_order) + '\n')


    # Доставка
    print("Доставка на дом ")
    print("Доставка в магазин ")
    choice_delivery = input("Выберите тип доставки(1,2): ")
    if choice_delivery == "1":
        address = input("Введите адрес куда нужно доставить товар ")
        delivery_hom = DelivCourier(address=address)
        order.set_delivery(delivery=delivery_hom)
    else:
        shop_list = select(s for s in Shop)[:]
        for shop in shop_list:
            print(shop.address)

        choice_shop = int(input("Выбереите магазин(1,2) "))

        delivery_shop = DelivShop(shop=shop_list[choice_shop - 1])
        order.set_delivery(delivery_shop)

    # Оплата
    print("На месте ")
    print("Сразу")
    choice_payType = input("Выберете тип оплаты(1,2) ")
    if choice_payType == "1":
        pay_type = PayType(name="На месте")
        order.set_payType(pay_type)
        order.set_payed(False)
    else:
        pay_type = PayType(name="Сразу")
        order.set_payType(pay_type)
        order.set_payed(True)

    # Вывод чека
    print("Чек")
    print("\t" + order.get_client().get_name() + " - имя заказчика")
    print("\t" + str(order.get_date()) + " - дата и время заказа")
    print("\t" + order.get_PayType().get_name() + " - тип оплаты")
    print("\t" + str(order.get_payed()) + " - подтверждение оплаты")

    print("\n\tТовары которые вы заказали:\n")

    for i in order.get_basket().get_products():
        print('\t' + i.get_productType().get_nameType() + " " + str(i.get_size()) + " " + i.get_color())

    print("\n\t" + str(order.get_basket().get_price()) + " рублей стоят товары в вашей корзине")
