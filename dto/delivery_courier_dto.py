from dto.delivery_dto import DeliveryDTO


class DeliveryCourierDTO(DeliveryDTO):
    def __init__(self, id=None, address=None, order=None, date=None):
        super().__init__(id, order, date)
        self.address = address

    def __str__(self):
        return f"Delivery address:{self.address}"

    '''
        def to_dict(self):
            d = super().to_dict()
            d['classtype'] = 'DeliveryCourier'
            return d
    '''
