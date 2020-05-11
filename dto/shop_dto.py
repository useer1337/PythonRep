from dto.dto import DTO


class ShopDTO(DTO):
    def __init__(self, id=None, address=None):
        self.id = id
        self.address = address

    def __str__(self):
        return f"Shop address:{self.address}"
