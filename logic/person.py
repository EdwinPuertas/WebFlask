class Person(object):

    def __init__(self, id_person: int, name: str = 'Name', last_name: str = "LastName"):
        self._id_person = id_person
        self._name = name
        self._last_name = last_name

    @property
    def id_person(self):
        return self._id_person

    @id_person.setter
    def name(self, id_person: int):
        self._id_person = id_person

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name: str):
        self._last_name = last_name

    def __str__(self):
        return '({0}, {1}, {2})'.format(self.id_person, self.name, self.last_name)


if __name__ == '__main__':
    edwin = Person(id_person=73577376, name="Edwin", last_name="Puertas")
    edwin.name = "Edwin. A"
    print(edwin)

