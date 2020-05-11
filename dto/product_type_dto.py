from dto.dto import DTO


class ProductTypeDTO(DTO):

    def __init__(self, id=None, name=None, product_type=None):
        self.id = id
        self.name = name
        self.product_type = product_type

    def __str__(self):
        return f"Product type id:{self.id}, name:{self.name}, parent_type:{self.product_type}"

    @staticmethod
    def class_by_name(name):
        global classes
        return classes[name]

classes = {'product_type': ProductTypeDTO}
