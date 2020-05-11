from datetime import datetime, timedelta

import dto.order_dto as OrderDTO
from dto.dto import DTO


class DeliveryDTO(DTO):
    classes = {'order': OrderDTO}

    # class_type=None
    def __init__(self, id=None, order=None, date=None):
        self.id = id
        self.order = order
       # self.class_type = class_type
        self.date = date


    @staticmethod
    def class_by_name(name):
        return DeliveryDTO.classes[name]
