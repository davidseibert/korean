# coding: utf-8

from korean.morphophonemics import phonology


class Morpheme(object):
    allomorphs = [None]
    def __init__(self):
        self.default_allomorph = self.allomorphs[0]
        self.current_allomorph = self.default_allomorph
        self.analyze()

    def spellout(self):
        text = ''.join([i.spellout() for i in self.syllables])
        return text

    def analyze(self):
        if self.allomorphs[0]:
            self.syllables = [phonology.Syllable(i) for i in self.current_allomorph]


class Stem(Morpheme):
    def __init__(self, input):
        self.input = input
        super(Stem, self).__init__()

    def analyze(self):
        self.syllables = [phonology.Syllable(i) for i in self.input]

class Affix(Morpheme):
    pass

class ConstantSuffix(Affix):
    def set_allomorph(self, node):
        pass

class AlternatingSuffix(Morpheme):
    def set_allomorph(self, node):
        tail = node.has_tail()
        if tail:
            self.current_allomorph = self.allomorphs[1]
        self.analyze()

class NomSuffix(AlternatingSuffix):
    allomorphs = [u'가', u'이']
class AccSuffix(AlternatingSuffix):
    allomorphs = [u'를', u'을']
class LocSuffix(ConstantSuffix):
    allomorphs = [u'에서']
