# coding: utf-8

leads = [u'ㄱ', u'ㄲ', u'ㄴ', u'ㄷ', u'ㄸ', u'ㄹ', u'ㅁ', u'ㅂ', u'ㅃ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅉ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

vowels = [u'ㅏ', u'ㅐ', u'ㅑ', u'ㅒ', u'ㅓ', u'ㅔ', u'ㅕ', u'ㅖ', u'ㅗ', u'ㅘ', u'ㅙ', u'ㅚ', u'ㅛ', u'ㅜ', u'ㅝ', u'ㅞ', u'ㅟ', u'ㅠ', u'ㅡ', u'ㅢ', u'ㅣ']

tails = [None, u'ㄱ', u'ㄲ', u'ㄳ', u'ㄴ', u'ㄵ', u'ㄶ', u'ㄷ', u'ㄹ', u'ㄺ', u'ㄻ', u'ㄼ', u'ㄽ', u'ㄾ', u'ㄿ', u'ㅀ', u'ㅁ', u'ㅂ', u'ㅄ', u'ㅅ', u'ㅆ', u'ㅇ', u'ㅈ', u'ㅊ', u'ㅋ', u'ㅌ', u'ㅍ', u'ㅎ']

BASE_OFFSET = 44032        
TAIL_PERIOD = len(tails)
RHYME_PERIOD = TAIL_PERIOD * len(vowels)

def unpack(input):
    normalized_code_point = ord(input) - BASE_OFFSET
    tail = tails[normalized_code_point % TAIL_PERIOD]
    vowel = vowels[normalized_code_point % RHYME_PERIOD / TAIL_PERIOD]
    lead = leads[normalized_code_point / RHYME_PERIOD]
    return (tail, vowel, lead)

def pack(tail, vowel, lead):
    whole = RHYME_PERIOD * leads.index(lead) \
               + TAIL_PERIOD * vowels.index(vowel) \
               + tails.index(tail) \
               + BASE_OFFSET
    whole = unichr(whole)
    return whole
