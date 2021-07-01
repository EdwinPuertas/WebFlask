class Person(object):

    def __init__(self, name: str = 'Name', last_name: str = "LastName"):
        self._name = name
        self._last_name = last_name

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
        return '{1}, {0}'.format(self.name, self.last_name)


if __name__ == '__main__':
    edwin = Person(name="Edwin", last_name="Puertas")
    edwin.name = "Edwin. A"
    print(edwin)

