from abc import ABC


class DTO(ABC):
    def set(self, **kwargs):
        for k, v in kwargs.items():
            if isinstance(v, dict):
                attribute = getattr(self, k)
                # костылёк
                if attribute:
                    attribute.set(**v)
            elif isinstance(v, list):
                attribute = getattr(self, k)
                for a, val in zip(attribute, v):
                    a.set(**val)
            else:
                setattr(self, k, v)

    @staticmethod
    def class_by_name(name):
        pass

    def to_dict(self):
        d = {}
        for k, v in self.__dict__.items():
            if isinstance(v, DTO):
                d[k] = v.to_dict()
            elif isinstance(v, list):
                d[k] = list(map(lambda item: item.to_dict(), v))

            else:
                d[k] = v
        return d

    @classmethod
    def from_dict(cls, d):
        param = {}
        for k, v in d.items():
            if isinstance(v, dict):
                klass = cls.class_by_name(k)
                param[k] = klass.from_dict(v)
            elif isinstance(v, list):
                klass = cls.class_by_name(k)
                param[k] = list(map(lambda item: klass.from_dict(item), v))
            else:
                param[k] = v

        return cls(**param)
