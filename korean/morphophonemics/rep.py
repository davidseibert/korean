# coding: utf-8

from suffixes import Nom, Acc, Loc
import suffixes
from syllable import break_word_into_syllables

class MorphophonemicRepresentation(object):
    def __init__(self, words):
        self.words = words
        self.syllabification()
        self.inflection()

    def export(self):
        return self

    def syllabification(self):
        for word in self.words:
            word.syllables = break_word_into_syllables(word)

    def inflection(self):
        for word in self.words:
            if hasattr(word, 'case'):
                getattr(suffixes, word.case)().add_to(word)

    def flatten_word(self, word):
        text = ''.join([s.spellout() for s in word.syllables])
        return text

    def flatten_sentence(self):
        text = ' '.join(self.flatten_word(w) for w in self.words)
        return text
