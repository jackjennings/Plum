from mojo.events import addObserver, removeObserver

from plum import Plum


class PlumObserver(object):

    def __init__(self):
        addObserver(self, 'update', 'currentGlyphChanged')
        addObserver(self, 'update', 'draw')

    def update(self, info):
        Plum(info['glyph']).update()
