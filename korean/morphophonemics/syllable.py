# coding: utf-8

from hangul import *

def break_word_into_syllables(word):
    syllables = [Syllable(i) for i in word.stem]
    return syllables

class Syllable (object):
    def __init__(self, literal):
        self.input = literal
        self.lead = None
        self.vowel = None
        self.tail = None
        
        self.analyze()
        self.synthesize()
    
    def spellout(self):
        return self.whole
        
    def has_tail(self):
        return self.tail

    def analyze(self):        
        normalized_code_point = ord(self.input) - BASE_OFFSET
        
        self.tail = tails[normalized_code_point % TAIL_PERIOD]
        self.vowel = vowels[normalized_code_point % RHYME_PERIOD / TAIL_PERIOD]
        self.lead = leads[normalized_code_point / RHYME_PERIOD]
        
        self.components = (
            self.lead,
            self.vowel,
            self.tail
            )
    
    def synthesize(self):
        self.whole = RHYME_PERIOD * leads.index(self.lead) \
                   + TAIL_PERIOD * vowels.index(self.vowel) \
                   + tails.index(self.tail) \
                   + BASE_OFFSET
        self.whole = unichr(self.whole)