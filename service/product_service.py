from dto.product_dto import ProductDTO
from dto.product_type_dto import ProductTypeDTO
from repository.product_repository import ProductRepository
from repository.product_type_repository import ProductTypeRepository
from service.service import CRUDService


class ProductService(CRUDService):
    def __init__(self):
        super().__init__(ProductDTO, ProductRepository())
        self.product_type_repository = ProductTypeRepository()

    def load_product_type(self, event):
        if event.product_type:
            event.product_type = ProductTypeDTO.from_dict(
                self.product_type_repository.find(event.product_type.id))
