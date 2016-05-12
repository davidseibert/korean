# coding: utf-8

import unicodedata

one = '가'

print one # 가

print len(one) # 3

print repr(one) # '\xea\xb0\x80'

print type(one) # <type 'str'>

two = one.decode('utf-8')

print two # 가

print len(two) # 1

print repr(two) # u'\uac00'

print type(two) # <type 'unicode'>

print ord(two)

three = u'가'

print three # 가

print len(three) # 1

print repr(three) # u'\uac00'

print type(three) # <type 'unicode'>

print unicodedata.name(three) # HANGUL SYLLABLE GA

print unicodedata.category(three) # Lo

print unicodedata.combining(three) # 0

print unicodedata.decomposition(three)

"""
D7FF)
Hangul Syllables Area	Edit
To find Hangul Syllables in Unicode, you can apply a simple formula. The formula and tables are as follows:

[{(initial) × 588} + {(medial) × 28} + (final)] + 44032
Initial Jamo	Edit
ㄱ 0
ㄲ 1
ㄴ 2
ㄷ 3
ㄸ 4
ㄹ 5
ㅁ 6
ㅂ 7
ㅃ 8
ㅅ 9
ㅆ 10
ㅇ 11
ㅈ 12
ㅉ 13
ㅊ 14
ㅋ 15
ㅌ 16
ㅍ 17
ㅎ 18
Medial Jamo	Edit
ㅏ 0
ㅐ 1
ㅑ 2
ㅒ 3
ㅓ 4
ㅔ 5
ㅕ 6
ㅖ 7
ㅗ 8
ㅘ 9
ㅙ 10
ㅚ 11
ㅛ 12
ㅜ 13
ㅝ 14
ㅞ 15
ㅟ 16
ㅠ 17
ㅡ 18
ㅢ 19
ㅣ 20
Final Jamo	Edit
no jamo 0
ㄱ 1
ㄲ 2
ㄳ 3
ㄴ 4
ㄵ 5
ㄶ 6
ㄷ 7
ㄹ 8
ㄺ 9
ㄻ 10
ㄼ 11
ㄽ 12
ㄾ 13
ㄿ 14
ㅀ 15
ㅁ 16
ㅂ 17
ㅄ 18
ㅅ 19
ㅆ 20
ㅇ 21
ㅈ 22
ㅊ 23
ㅋ 24
ㅌ 25
ㅍ 26
ㅎ 27
Example	Edit
For example, If you want to find the codepoint of “한” in Unicode:

The value of initial Jamo ㅎ is 18
The value of medial Jamo ㅏ is 0
The value of final Jamo ㄴ is 4
So, the formula will be {(18 × 588) + (0 × 28) + 4} + 44032, and the result is 54620. It means the Unicode value of 한 is 54620 in decimal, &#54620; by the numeric character reference, and U+D55C in standard Unicode notation.
"""

