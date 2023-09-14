from modules.LibraryItem import LibaryItem

class Magazine(LibaryItem):

    def __init__(self, title, upc, subject, volume, issue):
        LibaryItem.__init__(self, title, upc, subject)
        self.volume = volume
        self.issue = issue