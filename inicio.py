# INE 5404-02208A - Programação Orientada a Objetos II
# Gustavo Corrêa da Cunha (19203743)
# Felipe de Souza Goulart (19200417)
# coding: utf-8

class Book():

    def __init__(self, id, title, author, year, category, pages, language, publisher):
        
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.category = category
        self.pages = pages
        self.language = language
        self.publisher = publisher

    def getId(self):
        return self.id

    def setId(self, newId):
        self.id = newId

    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def getAuthor(self):
        return self.author

    def setAuthor(self, newAuthor):
        self.author = newAuthor

    def getYear(self):
        return self.year
    
    def setYear(self, newYear):
        self.year = newYear

    def getCategory(self):
        return self.category

    def setCategory(self, newCategory):
        self.category = newCategory

    def getPages(self):
        return self.pages

    def setPages(self, newPages):
        self.id = newPages

    def getLanguage(self):
        return self.language

    def setLanguage(self, newLanguage):
        self.language = newLanguage

    def getPublisher(self):
        return self.publisher

    def setPublisher(self, newPublisher):
        self.publisher = newPublisher

        