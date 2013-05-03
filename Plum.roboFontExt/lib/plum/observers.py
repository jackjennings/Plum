from plum.models import Plum
from mojo.events import addObserver, removeObserver

class PlumObserver(object):
    
    def __init__(self):
        addObserver(self, 'update', 'currentGlyphChanged')
        addObserver(self, 'update', 'draw')
        
    def update(self, info):
        Plum(info['glyph']).update()
