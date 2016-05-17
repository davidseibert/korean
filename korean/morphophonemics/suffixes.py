# coding: utf-8

from syllable import Syllable

def has_tail(word):
    return word.syllables[-1].has_tail()

class Suffix(object):
    def add_syllable(self, word, allomorph):
        for i in allomorph:
            word.syllables.append(Syllable(i))

class ConstantSuffix(Suffix):
    def add_to(self, word):
        self.add_syllable(word, self.allomorph)

class AlternatingSuffix(Suffix):
    def add_to(self, word):
        if has_tail(word):
            self.add_syllable(word, self.allomorphs[0])
        else:
            self.add_syllable(word, self.allomorphs[1])

class Nom(AlternatingSuffix):
    allomorphs = (u'이', u'가')

class Acc(AlternatingSuffix):
    allomorphs = (u'을', u'를')

class Loc(ConstantSuffix):
    allomorph = u'에서'


