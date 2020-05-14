from datetime import datetime, timedelta

import dto.order_dto as OrderDTO
from dto.dto import DTO


class DeliveryDTO(DTO):
    classes = {'order': OrderDTO}

    def __init__(self, id=None, order=None, date=None):
        self.id = id
        self.order = order
        if date:
            self.date = date
        else:
            self.date = datetime.now() + timedelta(days=10)

    @staticmethod
    def class_by_name(name):
        return DeliveryDTO.classes[name]
