# coding: utf-8

from korean.morphophonemics import phonology
from korean.utils import helpers

class Morpheme(helpers.Mixin):
    CONSOLE_COLOR = helpers.MORPHEME_CONSOLE_COLOR
    
    def __init__(self, input):
        self.input = input

class Root(Morpheme):
    pass

class Affix(Morpheme):
    pass
    

class Word (helpers.Mixin):
    CONSOLE_COLOR = helpers.WORD_CONSOLE_COLOR
    
    def __init__(self, input):
        self.input = input
                         
    def __str__(self):
        self.analyze()
        self.synthesize()
        return ''.join([str(i) for i in self.syllables])
    
    def analyze(self):
        self.syllables = [phonology.Syllable(i) for i in self.input]        
    
    def has_tail(self):
        return self.syllables[-1].has_tail()
    
    def debug(self):
        print self.input, '-->'
        
class Noun (Word):

    def set_case(self, case):
        self.case = case
    
    def synthesize(self):
        self.inflect()

    def inflect(self):
        self.case.apply(self)

    
class Verb (Word):
    def synthesize(self):
        pass


def main():
    dave = Word(u'데이브')
    dave.debug()
    emma = Word(u'연정')
    emma.debug()
                        
if __name__ == '__main__': main()
