class Plum(object):
    
    def __init__(self, glyph):
        self.glyph = glyph
        
    def toggle(self):
        if self.glyph is not None:
            if self._plum():
                self.destroy()
            else:
                self.create()
        
    def create(self):
        self.glyph.addGuide(self._position(), self._angle(), name="plum")
        
    def destroy(self):
        self.guide = self.glyph.removeGuide(self._plum())
        
    def update(self):
        if self.glyph:
            guide = self._plum()
            if guide:
                guide.x = self._position()[0]
        
    def _plum(self):
        return next((guide for guide in self.glyph.guides if guide.name is 'plum'), None)
        
    def _angle(self):
        return 90 + (CurrentFont().info.italicAngle or 0)
        
    def _position(self):
        return (self.glyph.width / 2, 0)

Plum(CurrentGlyph()).toggle()