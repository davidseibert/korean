# coding: utf-8

from utils.helpers import CONSOLE_FONT, SYLLABLE_CONSOLE_COLOR
from utils import helpers

leads = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

vowels = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

tails = [None, u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

BASE_OFFSET = 44032        
TAIL_PERIOD = len(tails)
RHYME_PERIOD = TAIL_PERIOD * len(vowels)
DEBUG = False
PYTHONISTA = False
if PYTHONISTA:
    import console
    console.set_font(*CONSOLE_FONT)

class Syllable (object):
    def __init__(self, syl):
        self.input = syl
        self.lead = None
        self.vowel = None
        self.tail = None
        
        self.analyze()
        self.synthesize()
        if DEBUG:
            self.show_processing()
    
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
    
    def show_processing(self):
        if PYTHONISTA:
            console.set_color(*SYLLABLE_CONSOLE_COLOR)
        print self.input, '-->', self.lead, self.vowel, self.tail, '-->', self.whole
        
def main():
    bing = Syllable(u'빙')
    moon = Syllable(u'문') 
                        
if __name__ == '__main__': main()
