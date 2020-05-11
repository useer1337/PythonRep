from dto.product_type_dto import ProductTypeDTO
from repository.product_type_repository import ProductTypeRepository
from service.service import CRUDService


class ProductTypeService(CRUDService):
    def __init__(self):
        super().__init__(ProductTypeDTO, ProductTypeRepository())
        self.product_type_repository = ProductTypeRepository()

    def load_product_type(self, event):
        if event.product_type and event.product_type.id:
            event.product_type = ProductTypeDTO.from_dict(
                self.product_type_repository.find(event.product_type.id))
