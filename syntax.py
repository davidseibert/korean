# coding: utf-8

from morphology import Noun, Verb

class Case (object):
    pass        
class Nominative (Case):
    pass
class Accusative (Case):
    pass
class Locative (Case):
    pass
    
class Sentence (object):
    def __init__(self, subject=None, object=None, location=None, verb=None):
        self.subject = subject
        self.object = object
        self.location = location
        self.verb = verb
        
        self.analyze()
        
    def analyze(self):
        pass   
        
    def flatten(self):
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
    eat = Verb(u'머거요')
    
    s1 = Sentence(subject=emma, verb=eat)
    print s1.flatten()
                        
if __name__ == '__main__': main()
        