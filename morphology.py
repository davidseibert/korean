# coding: utf-8

from helpers import CONSOLE_FONT, MORPHEME_CONSOLE_COLOR, WORD_CONSOLE_COLOR

import phonology

DEBUG = False
PYTHONISTA = True
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
        
        self.analyze()
        
        if DEBUG:
            self.show_processing()
    
    def __str__(self):
        return ''.join([str(i) for i in self.syllables])
    
    def analyze(self):
        self.syllables = [phonology.Syllable(i) for i in self.input]        
    
    def set_case(self, case):
        self.case = case
    
    def show_processing(self):
        if PYTHONISTA:
            console.set_color(*WORD_CONSOLE_COLOR)
        print self.input, '-->'

class Noun (Word):
    pass
    
class Verb (Word):
    pass


def main():
    dave = Word(u'데이브')
    emma = Word(u'연정')
                        
if __name__ == '__main__': main()