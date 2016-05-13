# coding: utf-8

class Graph(object):
    pass
class Allograph(object):
    pass
class Grapheme(object):
    def __init__(self, name, romanization, lead_hex, vowel_hex, tail_hex):
		self.name = name
		self.romanization = romanization

                #Name           #Roman  #Onset  #Nucleus    #Coda       #Spec
jamo = [
    Grapheme(   'kiyeok',       'g',    0x1100, None,       0x11a8,  ), # ㄱ
    Grapheme(   'ssangkiyeok',  'gg',   0x1101, None,       0x11a9,  ), # ㄲ
    Grapheme(   'kiyeok-sios',  'gs',   None,   None,       0x11aa,  ), # ᆪ
    Grapheme(   'nieun',        'n',    0x1102, None,       0x11ab,  ), # ㄴ
    Grapheme(   'nieun-cieuc',  'nj',   None,   None,       0x11ac,  ), # ᆬ
    Grapheme(   'nieun-hieuh',  'nh',   None,   None,       0x11ad,  ), # ᆭ
    Grapheme(   'tikeut',       'd',    0x1103, None,       0x11ae,  ), # ㄷ
    Grapheme(   'ssangtikeut',  'dd',   0x1104, None,       None,    ), # ㄸ
    Grapheme(   'rieul',        'r',    0x1105, None,       0x11af,  ), # ㄹ
    Grapheme(   'rieul-kiyeok', 'lg',   None,   None,       0x11b0,  ), # ᆰ
    Grapheme(   'rieul-mieum',  'lm',   None,   None,       0x11b1,  ), # ᆱ
    Grapheme(   'rieul-pieup',  'lb',   None,   None,       0x11b2,  ), # ᆲ
    Grapheme(   'rieul-sios',   'ls',   None,   None,       0x11b3,  ), # ᆳ
    Grapheme(   'rieul-thieuth','lt',   None,   None,       0x11b4,  ), # ᆴ
    Grapheme(   'rieul-phieuph','lp',   None,   None,       0x11b5,  ), # ᆵ
    Grapheme(   'rieul-hieuh',  'lh',   None,   None,       0x11b6,  ), # ᆶ
    Grapheme(   'mieum',        'm',    0x1106, None,       0x11b7,  ), # ㅁ
    Grapheme(   'pieup',        'b',    0x1107, None,       0x11b8,  ), # ㅂ
    Grapheme(   'pieup-sios',   'bs',   None,   None,       0x11b9,  ), # ᆹ
    Grapheme(   'ssangpieup',   'bb',   0x1108, None,       None,    ), # ㅃ
    Grapheme(   'sios',         's',    0x1109, None,       0x11ba,  ), # ㅅ
    Grapheme(   'ssangsios',    'ss',   0x110a, None,       0x11bb,  ), # ㅆ
    Grapheme(   'ieung',        'ng',   0x110b, None,       0x11bc,  ), # ㅇ
    Grapheme(   'cieuc',        'j',    0x110c, None,       0x11bd,  ), # ㅈ
    Grapheme(   'ssangcieuc',   'jj',   0x110d, None,       None,    ), # ㅉ
    Grapheme(   'chieuch',      'c',    0x110e, None,       0x11be,  ), # ㅊ
    Grapheme(   'khieukh',      'k',    0x110f, None,       0x11bf,  ), # ㅋ
    Grapheme(   'thieuth',      't',    0x1110, None,       0x11c0,  ), # ㅌ
    Grapheme(   'phieuph',      'p',    0x1111, None,       0x11c1,  ), # ㅍ
    Grapheme(   'hieuh',        'h',    0x1112, None,       0x11c2,  ), # ㅎ
    Grapheme(   'a',            'a',    None,   0x1161,     None,    ), # ㅏ
    Grapheme(   'ae',           'ae',   None,   0x1162,     None,    ), # ㅐ
    Grapheme(   'ya',           'ya',   None,   0x1163,     None,    ), # ㅑ
    Grapheme(   'yae',          'yae',  None,   0x1164,     None,    ), # ㅒ
    Grapheme(   'eo',           'eo',   None,   0x1165,     None,    ), # ㅓ
    Grapheme(   'e',            'e',    None,   0x1166,     None,    ), # ㅔ
    Grapheme(   'yeo',          'yeo',  None,   0x1167,     None,    ), # ㅕ
    Grapheme(   'ye',           'ye',   None,   0x1168,     None,    ), # ㅖ
    Grapheme(   'o',            'o',    None,   0x1169,     None,    ), # ㅗ
    Grapheme(   'wa',           'wa',   None,   0x116a,     None,    ), # ㅘ
    Grapheme(   'wae',          'wae',  None,   0x116b,     None,    ), # ㅙ
    Grapheme(   'oe',           'oe',   None,   0x116c,     None,    ), # ㅚ
    Grapheme(   'yo',           'yo',   None,   0x116d,     None,    ), # ㅛ
    Grapheme(   'u',            'u',    None,   0x116e,     None,    ), # ㅜ
    Grapheme(   'weo',          'weo',  None,   0x116f,     None,    ), # ㅝ
    Grapheme(   'we',           'we',   None,   0x1170,     None,    ), # ㅞ
    Grapheme(   'wi',           'wi',   None,   0x1171,     None,    ), # ㅟ
    Grapheme(   'yu',           'yu',   None,   0x1172,     None,    ), # ㅠ
    Grapheme(   'eu',           'eu',   None,   0x1173,     None,    ), # ㅡ
    Grapheme(   'yi',           'yi',   None,   0x1174,     None,    ), # ㅢ
    Grapheme(   'i',            'i',    None,   0x1175,     None,    ), # ㅣ
]

def main():
    pass
                        
if __name__ == '__main__': main()
        

