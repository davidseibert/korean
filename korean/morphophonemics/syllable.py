# coding: utf-8

import hangul

def break_word_into_syllables(word):
    syllables = [Syllable(i) for i in word.stem]
    return syllables

class Syllable (object):
    def __init__(self, literal):
        self.input = literal

        self.analyze()
        self.synthesize()
    
    def spellout(self):
        return self.whole
        
    def has_tail(self):
        return self.tail

    def analyze(self):        
        self.tail, self.vowel, self.lead = hangul.unpack(self.input)
    
    def synthesize(self):
        self.whole = hangul.pack(self.tail, self.vowel, self.lead)
