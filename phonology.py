# coding: utf-8

from helpers import CONSOLE_FONT, SYLLABLE_CONSOLE_COLOR

leads = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

vowels = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

tails = [None, 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

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
    
    def __str__(self):
        return self.whole.encode('utf-8')
        
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
