# coding: utf-8

from syntax import Propn, Place, Noun, TransitiveVerb
from morphology import Stem

class Emma(Propn):
    stem = Stem(u'연정')
class Elly(Propn):
    stem = Stem(u'엘리')
class Dave(Propn):
    stem = Stem(u'데이브')
class House(Place):
    stem = Stem(u'집')
class Treat(Noun):
    stem = Stem(u'트리트')
class Lunch(Noun):
    stem = Stem(u'점심')
class Eat(TransitiveVerb):
    stem = Stem(u'머거요')
