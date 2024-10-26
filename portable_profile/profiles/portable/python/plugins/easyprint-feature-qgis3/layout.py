# -*- coding: utf-8 -*-


class Layout:
    def __init__(self, id):
        self.id = id
        self.orientation = "portrait"
        self.margins = [0, 0, 0, 0]
        self.decorations = []

    def setOrientation(self, ori):
        self.orientation = ori

    def setMargins(self, m):
        self.margins = m

    def addDecoration(self, d):
        self.decorations.append(d)

    def getID(self):
        return self.id

    def getOrientation(self):
        return self.orientation

    def getMargins(self):
        margins = {
            "margin-top": self.margins[0],
            "margin-right": self.margins[1],
            "margin-bottom": self.margins[2],
            "margin-left": self.margins[3],
        }
        return margins

    def getDecorations(self):
        return self.decorations
