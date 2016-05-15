# coding: utf-8

class PartOfSpeech(object):
    pass

# Open
class Adj(PartOfSpeech):
    """Adjective"""
    pass
class Adv(PartOfSpeech):
    """Adverb"""
    pass
class Intj(PartOfSpeech):
    """Interjection"""
    pass
class Noun(PartOfSpeech):
    """Noun"""
    pass
class Propn(Noun):
    """Proper Noun"""
    pass
class Verb(PartOfSpeech):
    """Verb"""
    pass

#Closed
class Adp(PartOfSpeech):
    """Adposition"""
    pass
class Aux(PartOfSpeech):
    """Auxiliary Verb"""
    pass
class Conj(PartOfSpeech):
    """Coordinating Conjunction"""
    pass
class Det(PartOfSpeech):
    """Determiner"""
    pass
class Num(PartOfSpeech):
    """Numeral"""
    pass
class Part(PartOfSpeech):
    """Particle"""
    pass
class Pron(Noun):
    """Pronoun"""
    pass
class Sconj(PartOfSpeech):
    """Subordinating Conjunction"""
    pass

#Other
class Punct(PartOfSpeech):
    """Punctuation"""
    pass
class Sym(PartOfSpeech):
    """Symbol"""
    pass
class X(PartOfSpeech):
    """Other"""
    pass
