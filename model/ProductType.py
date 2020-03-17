class ProductType:
    def __init__(self, name: str, parent_type = None):
        self.name = name
        self.parent_type = parent_type

    def set_nameType(self, name: str):
        self.name = name

    def set_parentType(self, parent_type):
        self.parent_type = parent_type

    def get_nameType(self):
        return self.name

    def get_parentType(self):
        return self.parent_type
