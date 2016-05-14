# coding: utf-8

class PartOfSpeech(object):
    pass

# Open
class ADJ(PartOfSpeech):
    """Adjective"""
    pass
class ADV(PartOfSpeech):
    """Adverb"""
    pass
class INTJ(PartOfSpeech):
    """Interjection"""
    pass
class NOUN(PartOfSpeech):
    """Noun"""
    pass
class PROPN(NOUN):
    """Proper Noun"""
    pass
class VERB(PartOfSpeech):
    """Verb"""
    pass

#Closed
class ADP(PartOfSpeech):
    """Adposition"""
    pass
class AUX(PartOfSpeech):
    """Auxiliary Verb"""
    pass
class CONJ(PartOfSpeech):
    """Coordinating Conjunction"""
    pass
class DET(PartOfSpeech):
    """Determiner"""
    pass
class NUM(PartOfSpeech):
    """Numeral"""
    pass
class PART(PartOfSpeech):
    """Particle"""
    pass
class PRON(NOUN):
    """Pronoun"""
    pass
class SCONJ(PartOfSpeech):
    """Subordinating Conjunction"""
    pass

#Other
class PUNCT(PartOfSpeech):
    """Punctuation"""
    pass
class SYM(PartOfSpeech):
    """Symbol"""
    pass
class X(PartOfSpeech):
    """Other"""
    pass
