from typing import List

from logic.Document import Document
from logic.Person import Person


class Book(Document):
    """
    Class used to represent a Book
    """
    def __init__(self, code: str = "0000000", title: str = "Document Title", editorial: str = "Editorial",
                 edition: int = 1, theme: str = "General", language: str = "EN", pages: int = 1,
                 authors: List[Person] = None, isbn: str = "XXXX-XXXX"):
        """ Book constructor object.
        :param isbn: isbn of document.
        :type isbn: str
        """
        super().__init__(code, title, editorial, edition, theme, language, pages, authors)
        self.__isbn = isbn

    @property
    def isbn(self):
        """ Returns the isbn of the document.
        :returns: isbn of document.
        :rtype: str
        """
        return self.__isbn

    @isbn.setter
    def isbn(self, isbn: str):
        """ The isbn of the document is assigned.
        :param isbn: isbn of the document.
        :type: str
        """
        self.__isbn = isbn

    def __str__(self):
        return super(Book, self).__str__() + '\nISBN: {0}'.format(self.isbn)


if __name__ == '__main__':
    from logic.Person import Person

    aut1 = Person(name="Christopher", last_name="M.Bishop")
    book = Book(code="0387310738", title="Pattern Recognition and Machine Learning", editorial="Springer",
                pages=738, authors=[aut1], theme="Information Science and Statistics", isbn="978-0387310732")

    print(book)