class Service:
    def __init__(self, cls, repository):
        self.repository = repository
        self.cls = cls

    def from_collection_dict(self, collection):
        return list(map(self.cls.from_dict, collection))


class ROService(Service):
    def get_all(self):
        return self.from_collection_dict(self.repository.all())

    def get_by_id(self, id):
        return self.cls.from_dict(self.repository.find(id))


class CRUDService(ROService):
    def create(self, obj):
        obj.set(**self.repository.create(obj.to_dict()))

    def update(self, obj):
        obj.set(**self.repository.update(obj.to_dict()))

    def delete(self, obj):
        self.repository.delete(obj.id)
