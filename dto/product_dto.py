from dto.dto import DTO
from dto.product_type_dto import ProductTypeDTO


class ProductDTO(DTO):
    classes = {'product_type': ProductTypeDTO}

    def __init__(self, id=None, size=None, color=None, price=None,
                 quantity=None, product_type=None):
        self.id = id
        self.size = size
        self.color = color
        self.price = price
        self.quantity = quantity
        self.product_type = product_type

    def __str__(self):
        return f"Product: id:{self.id} size:{self.size}  color:{self.color} price:{self.price} quantity:{self.quantity} product_type:{self.product_type}"

    @staticmethod
    def class_by_name(name):
        return ProductDTO.classes[name]