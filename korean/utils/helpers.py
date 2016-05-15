# coding: utf-8

import sys

# Switches

PYTHONISTA = (sys.platform == 'iphoneos')
DEBUG = True

def same(test_case, one, two):
    test_case.assertEqual(one, two,
        msg="\nTarget: '{}'\nResult: '{}'".format(one.encode('utf-8'), two.encode('utf-8'))
                          )


# Console Config

CONSOLE_FONT = ('Source Code Pro', 18)
DEFAULT_CONSOLE_COLOR = (1.0, 1.0, 1.0) # white
MORPHEME_CONSOLE_COLOR = (.75, 1.0, .7) # light green
SYLLABLE_CONSOLE_COLOR = (.6, .74, 1.0) # light purple
WORD_CONSOLE_COLOR = (.99, 1.0, .8) # light yellow

if PYTHONISTA:
    import console
    console.set_font(*CONSOLE_FONT)
    

# Universal Mixin
    
class Mixin (object):
    CONSOLE_COLOR = DEFAULT_CONSOLE_COLOR
    
    def explain(self):
        self.configure_console()
        if DEBUG:
            self.show_processing()
    
    def configure_console(self):
        if PYTHONISTA:
            console.set_color(*self.CONSOLE_COLOR)

def print_heading(text):
    print text
    print "=" * len(text)
    print
