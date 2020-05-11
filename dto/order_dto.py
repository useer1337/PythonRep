import dto.basket_dto as BasketDTO
from dto.client_dto import ClientDTO
from dto.delivery_dto import DeliveryDTO
from dto.dto import DTO
from dto.pay_type_dto import PayTypeDTO


class OrderDTO(DTO):
    classes = {'client': ClientDTO,
               'pay_type': PayTypeDTO,
               'delivery': DeliveryDTO,  # TODO mb wrong type delivery
               'basket': BasketDTO
               }

    def __init__(self, id=None, payed=None, client=None, pay_type=None,
                 delivery=None, basket=None):
        self.id = id
        self.payed = payed
        self.client = client
        self.pay_type = pay_type
        self.delivery = delivery
        self.basket = basket

    def __str__(self):
        return f"Order  id:{self.id} payed:{self.payed}  client:{self.client}" \
                + f"pay_type:{self.pay_type} delivery:{self.delivery} basket:{self.basket}"


    @staticmethod
    def class_by_name(name):
        return OrderDTO.classes[name]
