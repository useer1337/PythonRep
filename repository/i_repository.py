from abc import ABC, abstractmethod


class IRORepository:
    @abstractmethod
    def find(self, id):
        pass

    @abstractmethod
    def all(self, **attrs):
        pass


class ICRUDRepository (IRORepository):
    @abstractmethod
    def create(self, instance):
        pass

    @abstractmethod
    def update(self, instance):
        pass

    @abstractmethod
    def delete(self, instance):
        pass

