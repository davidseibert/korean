# coding: utf-8

class Sentence (object):
    def __init__(self, **kwargs):
        self.raw_constituents = kwargs
        self.raw = self.raw_constituents
                
    def flatten(self):
        try:
            subject = self.raw['subject'] + self.raw['subject_particle']
        except KeyError:
            subject = None
        try:
            location = self.raw['location'] + self.raw['location_particle']       
        except KeyError:
            location = None
        try:
            object = self.raw['object'] + self.raw['object_particle']     
        except KeyError:
            object = None
                
        verb = self.raw['verb']
        
        parts = [subject, location, object, verb]
        
        sentence = ' '.join([
            part for part in parts if part
            ])
        return sentence
        
class Syllable (object):
    def __init__(self, syl):
        self.lead = None
        self.vowel = None
        self.tail = None
        
        self._analyze(syl)
        
    def _analyze(self, syl):
        _ord = ord(syl)
        print 'ord = {}'.format(_ord)
        print 'ord / 588 = {}'.format(_ord / 588)
        print 'ord % 588 = {}'.format(_ord % 588)
        
if __name__ == '__main__':
    pass
    s = Syllable(u'가')
    