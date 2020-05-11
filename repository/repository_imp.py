from abc import abstractmethod

from pony.orm import db_session, commit

from repository.i_repository import IRORepository, ICRUDRepository


class RORepositoryImp(IRORepository):

    @staticmethod
    @abstractmethod
    def to_dict(obj):
        pass

    @classmethod
    def to_collection_dict(cls, objs):
        return list(map(cls.to_dict, objs))

    def __init__(self, klass):
        self.klass = klass

    @db_session
    def find(self, id):
        return self.to_dict(self.klass.get(id=id))

    @db_session
    def all(self, **attrs):
        return self.to_collection_dict(self.klass.select(**attrs)[:])


class CRUDRepositoryImp(RORepositoryImp, ICRUDRepository):
    @staticmethod
    def from_dict(obj):
        return obj

    @db_session
    def create(self, obj):
        return self.to_dict(self.klass(**self.from_dict(obj)))

    @db_session
    def update(self, obj):
        d = self.from_dict(obj)
        entity = self.klass.get(id=d['id'])
        entity.set(**d)
        commit()
        return self.to_dict(entity)

    @db_session
    def delete(self, id):
        self.klass.get(id=id).delete()
