from modules.LibraryItem import LibaryItem

class Dvd(LibaryItem):

    def __init__(self, title, upc, subject, actors, directors, genre):
        LibaryItem.__init__(self, title, upc, subject)
        self.actors = actors
        self.directors = directors
        self.genre = genre