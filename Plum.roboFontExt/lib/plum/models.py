class Plum(object):
    
    def __init__(self, glyph):
        self.glyph = glyph
        
    def toggle(self):
        if self.glyph is not None:
            if self._getPlum():
                self.destroy()
            else:
                self.create()
        
    def create(self):
        self.glyph.addGuide((self.glyph.width / 2, 0), 90, name="plum")
        
    def destroy(self):
        self.guide = self.glyph.removeGuide(self._getPlum())
        
    def update(self):
        if self.glyph:
            guide = self._getPlum()
            if guide:
                guide.x = self.glyph.width / 2
        
    def _getPlum(self):
        return next((guide for guide in self.glyph.guides if guide.name is 'plum'), None)
