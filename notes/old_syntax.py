# coding: utf-8

from korean.morphophonemics.phonology import Syllable
from notes.old_morphology import Noun, Verb


class Case (object):
    pass        

class Nominative (Case):
    def apply(self, noun):
        if noun.has_tail():
            noun.syllables.append(Syllable(u'이'))
        else:
            noun.syllables.append(Syllable(u'가'))

class Accusative (Case):
    def apply(self, noun):
        if noun.has_tail():
            noun.syllables.append(Syllable(u'을'))
        else:
            noun.syllables.append(Syllable(u'를'))

class Locative (Case):
    def apply(self, noun):
            noun.syllables.append(Syllable(u'에'))
            noun.syllables.append(Syllable(u'서'))
    
class Sentence (object):
    def __init__(self, subject=None, object=None, location=None, verb=None):
        self.subject = subject
        self.object = object
        self.location = location
        self.verb = verb
        
        self.assign_cases()
        self.analyze()

    def assign_cases(self):
        try:
            self.subject.set_case(Nominative())   
        except AttributeError:
            pass
        try:
            self.object.set_case(Accusative())   
        except AttributeError:
            pass
        try:
            self.location.set_case(Locative())   
        except AttributeError:
            pass
        
    def analyze(self):
        pass   
        
    def __str__(self):
        sentence = ' '.join([
            str(part) for part in [
                self.subject,
                self.location,
                self.object,
                self.verb,
                ] if part
            ])
        return sentence

def main():
    dave = Noun(u'데이브')
    emma = Noun(u'연정')
    elly = Noun(u'엘리')
    house = Noun(u'집')
    treat = Noun(u'트리트')
    lunch = Noun(u'점심')
    eat = Verb(u'머거요')
    s1 = Sentence(subject=emma, verb=eat)
    s2 = Sentence(subject=dave, object=lunch, verb=eat)
    s3 = Sentence(subject=elly, object=treat, location=house, verb=eat)
    print s1
    print s2
    print s3
                        
if __name__ == '__main__': main()
        
