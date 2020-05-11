from dto.delivery_dto import DeliveryDTO
from dto.shop_dto import ShopDTO


class DeliveryShopDTO(DeliveryDTO):
    classes = {'shop': ShopDTO}

    def __init__(self, id=None, order=None, shop=None, date=None):
        super().__init__(id, order, date)
        self.shop = shop

    def __str__(self):
        return f"DeliveryDTO = id:{self.id}  address:{self.order}"

    @staticmethod
    def class_by_name(name):
        return DeliveryShopDTO.classes[name]

    '''
        def to_dict(self):
            d = super().to_dict()
            d['classtype'] = 'DeliveryShop'
            return d

    '''
