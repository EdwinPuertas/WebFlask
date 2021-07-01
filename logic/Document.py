from logic.Person import Person
from typing import List


class Document(object):
    """
    Class used to represent a Document
    """

    def __init__(self, code: str = "0000000", title: str = "Document Title",
                 editorial: str = "Editorial", edition: int = 1, theme: str = "General",
                 language: str = "EN", pages: int = 1, authors: List[Person] = None):
        """ Document constructor object.
        :param code: code of document.
        :type code: str
        :param title: title of document.
        :type title: str
        :param editorial: editorial of document.
        :type editorial: str
        :param edition: edition of document.
        :type edition: int
        :param theme: theme of document.
        :type theme: str
        :param theme: theme of document.
        :type theme: str
        :param language: language of document.
        :type language: str
        :param pages: pages of document.
        :type pages: int
        :param authors: authors of document.
        :type authors: Person
        :returns: Document object
        :rtype: object
        """
        self.__code = code
        self.__title = title
        self.__editorial = editorial
        self.__edition = edition
        self.__theme = theme
        self.__language = language
        self.__pages = pages
        self.__authors = authors

    @property
    def code(self):
        """ Returns the code of the document.
        :returns: code of document.
        :rtype: str
        """
        return self.__code

    @code.setter
    def code(self, code: str):
        """ The code of the document is assigned.
        :param code: code of the document.
        :type: str
        """
        self.__code = code

    @property
    def title(self):
        """ Returns the title of the document.
        :returns: title of document.
        :rtype: str
        """
        return self.__title

    @title.setter
    def title(self, title: str):
        """ The title of the document is assigned.
        :param title: title of the document.
        :type: str
        """
        self.__title = title

    @property
    def editorial(self):
        """ Returns the editorial of the document.
        :returns: editorial of document.
        :rtype: str
        """
        return self.__editorial

    @editorial.setter
    def editorial(self, editorial: str):
        """ The editorial of the document is assigned.
        :param editorial: editorial of the document.
        :type: str
        """
        self.__editorial = editorial

    @property
    def edition(self):
        """ Returns the edition of the document.
        :returns: edition of document.
        :rtype: str
        """
        return self.__edition

    @edition.setter
    def edition(self, edition: int):
        """ The edition of the document is assigned.
        :param edition: edition of the document.
        :type: int
        """
        self.__edition = edition

    @property
    def theme(self):
        """ Returns the theme of the document.
        :returns: theme of document.
        :rtype: str
        """
        return self.__theme

    @theme.setter
    def theme(self, theme: str):
        """ The edition of the document is assigned.
        :param theme: edition of the document.
        :type: str
        """
        self.__theme = theme

    @property
    def language(self):
        """ Returns the language of the document.
        :returns: language of document.
        :rtype: str
        """
        return self.__language

    @language.setter
    def language(self, language: str):
        """ The language of the document is assigned.
        :param language: language of the document.
        :type: str
        """
        self.__language = language

    @property
    def pages(self):
        """ Returns the pages of the document.
        :returns: pages of document.
        :rtype: int
        """
        return self.__pages

    @pages.setter
    def pages(self, pages: int):
        """ The edition of the document is assigned.
        :param pages: pages of the document.
        :type: int
        """
        self.__pages = pages

    @property
    def authors(self):
        """ Returns author' list of the document.
        :returns: authors of document.
        :rtype: Person
        """
        val = []
        if self.__authors is not None:
            val = [a.__str__() for a in self.__authors]
        return val

    @authors.setter
    def authors(self, authors: List[Person]):
        """ Author' list of the document is assigned.
        :param authors: authors of the document.
        :type: Person
        """
        self.__authors = authors

    def __str__(self):
        name_class = type(self).__name__
        return '[Type - {0}]\n{1}\nCode: {2}\nTitle: {3}\nEditorial: {4}' \
               '\nEdition: {5}\nTheme: {6}\nLanguage: {7}' \
               '\nPages: {8}\nAuthors: {9}'.format(name_class, 30*"-", self.code, self.title,
                                                   self.editorial, self.edition, self.theme,
                                                   self.language, self.pages, self.authors)


if __name__ == '__main__':
    from logic.Person import Person

    aut1 = Person(name="Edwin", last_name="Puertas")
    doc = Document(code="0234456", title="New Document", editorial="Springer",
                   pages=100, authors=[aut1], theme="Statistics")
    print(doc)