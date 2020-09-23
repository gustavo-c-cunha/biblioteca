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

class User():
    def __init__(self, name, age, phone, email, address, cpf, admin):
        self.name = name
        self.age = age
        self.phone = phone
        self.email = email
        self.address = address
        self.cpf = cpf
        self.admin = admin
        
    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getAge(self):
        return self.age

    def setAge(self, newAge):
        self.age = newAge

    def getPhone(self):
        return self.phone

    def setPhone(self, newPhone):
        self.phone = newPhone

    def getEmail(self):
        return self.email

    def setEmail(self, newEmail):
        self.email = newEmail

    def getAddress(self):
        return self.address

    def setAddress(self, newAddress):
        self.address = newAddress
    
    def getCpf(self):
        return self.cpf
    
    def setCpf(self, newCpf):
        self.cpf = newCpf


class Author():
    def __init__(self, name):
        self.name = name
        self.books = []

    def getName(self):
        return self.name
    
    def setName(self, newName):
        self.name = newName

    def getBooks(self):
        for i in range(len(self.books)):
            return self.books[i].getTitle()

    def addBook(self, book):
        self.books.append(book)

    def delBook(self, book):
        self.books.remove(book)

class Publisher():
    def __init__(self, name, cnpj):
        self.name = name
        self.cnpj = cnpj
        self.books = []

    def getName(self):
        return self.name

    def setName(self, newName):
        self.name = newName

    def getCnpj(self):
        return self.cnpj

    def setCnpj(self, newCnpj):
        self.cnpj = newCnpj

    def getBooks(self):
        for i in range(len(self.books)):
            return self.books[i].getTitle()

    def addBook(self, book):
        self.books.append(book)

    def delBook(self, book):
        self.books.remove(book)

    