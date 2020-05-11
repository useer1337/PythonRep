from pony.orm import *

db = Database()


class Person(db.Entity):
    name = Required(str)
    cars = Set('Car')


class Car(db.Entity):
    make = Required(str)
    model = Required(str)
    owner = Optional(Person)


db.bind(provider='sqlite', filename='db_exmaple', create_db=True)
db.generate_mapping(create_tables=True)

with db_session:
    c1 = Car(make='Tayota', model='Camry')
    c2 = Car(make='Tayota1', model='Camry1')

    cars_set = {c1, c2}

    p1 = Person(name='John', cars=cars_set)

    print(p1.cars)