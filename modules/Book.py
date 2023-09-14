from modules.LibraryItem import LibaryItem

class Book(LibaryItem):

    def __init__(self, isbn, authors, title, subject, dds_number, upc):
        LibaryItem.__init__(self, title, upc, subject)
        self.isbn = isbn
        self.authors = authors
        self.dds_number = dds_number
