from dto.dto import DTO


class PayTypeDTO(DTO):
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Pay type name:{self.name}"
