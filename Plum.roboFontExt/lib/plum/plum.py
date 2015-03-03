GUIDE_NAME = 'plum'


class Plum(object):

    def __init__(self, glyph):
        self.glyph = glyph

    def toggle(self):
        if self.plum_guide:
            self.destroy()
        else:
            self.create()

    def create(self):
        if self.glyph_exists:
            self.glyph.addGuide(self.position, self.angle, name=GUIDE_NAME)

    def destroy(self):
        if self.glyph_exists:
            self.glyph.removeGuide(self.plum_guide)

    def update(self):
        if self.glyph_exists:
            guide = self.plum_guide
            if guide:
                guide.x = self.horizontal_center

    @property
    def guides(self):
        return self.glyph.guides if self.glyph_exists else []

    @property
    def plum_guides(self):
        return (guide for guide in self.guides if guide.name is GUIDE_NAME)

    @property
    def plum_guide(self):
        return next(self.plum_guides, None)

    @property
    def angle(self):
        return 90 + (self.font.info.italicAngle or 0)

    @property
    def position(self):
        return (self.glyph.width / 2, 0)

    @property
    def horizontal_center(self):
        return self.position[0]

    @property
    def font(self):
        return self.glyph.getParent()

    @property
    def glyph_exists(self):
        return self.glyph is not None
