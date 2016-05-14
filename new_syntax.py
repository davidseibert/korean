# coding: utf-8

class PartOfSpeech(object):
    def __init__(self, input):
        self.input = input
    
class Verb(PartOfSpeech):
    """Verb"""
    pass
    
class TransitiveVerb(Verb):
    """Transitive Verb"""
    
    def __call__(self, subject, object, loc=None):
        self.subject = subject
        self.object = object
        self.loc = loc
        return self

class Noun(PartOfSpeech):
    """Noun"""
    pass

class Propn(Noun):
    """Proper Noun"""
    pass

class Dependency(object):
    pass

class Nsubj(Dependency):
    pass

class Dobj(Dependency):
    pass

emma = Propn(u'연정')
dave = Propn(u'데이브')
eat = TransitiveVerb(u'머거요')
elly = Propn(u'엘리')
house = Noun(u'집')
treat = Noun(u'트리트')
lunch = Noun(u'점심')

sentence1 = eat(emma, lunch)
sentence2 = eat(dave, lunch)
sentence3 = eat(elly, treat, loc=house)

print sentence1.subject
print sentence2
print sentence3