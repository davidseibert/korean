# coding: utf-8

from helpers import CONSOLE_FONT, MORPHEME_CONSOLE_COLOR, WORD_CONSOLE_COLOR

import phonology

DEBUG = False
PYTHONISTA = False
if PYTHONISTA:
    import console
    console.set_font(*CONSOLE_FONT)

class Morpheme (object):
    def __init__(self, input):
        self.input = input
        
        if DEBUG:
            self.show_processing()
    
    def show_processing(self):
        if PYTHONISTA:
            console.set_color(MORPHEME_CONSOLE_COLOR)
        print self.input, '-->'
        

class Word (object):
    def __init__(self, input, case=None):
        self.input = input
        self.set_case(case)
        
        
        if DEBUG:
            self.show_processing()
    
    def __str__(self):
        self.analyze()
        self.synthesize()
        return ''.join([str(i) for i in self.syllables])
    
    def analyze(self):
        self.syllables = [phonology.Syllable(i) for i in self.input]        
    
    def set_case(self, case):
        self.case = case
    
    def has_tail(self):
        return self.syllables[-1].has_tail()

    def show_processing(self):
        if PYTHONISTA:
            console.set_color(*WORD_CONSOLE_COLOR)
        print self.input, '-->'

class Noun (Word):
    def synthesize(self):
        self.inflect()

    def inflect(self):
        self.case.apply(self)

    
class Verb (Word):
    def synthesize(self):
        pass


def main():
    dave = Word(u'데이브')
    emma = Word(u'연정')
                        
if __name__ == '__main__': main()
