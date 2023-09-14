from modules.LibraryItem import LibaryItem

class Cd(LibaryItem):

    def __init__(self, title, upc, subject, artist):
        LibaryItem.__init__(self, title, upc, subject)
        self.artist = artist
