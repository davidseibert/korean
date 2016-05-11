# coding: utf-8

import unittest

examples = {
    #1
    "Andrew eats lunch at home.":
    "앤드류가 집에서 점심을 머거요.",
    #2
    'How are you?':
    '안녕하십니까?',
    #3
    'What do you study?':
    '뭐 공부하세요?',
    #4
    'Thank you.':
    '감사합니다.',
    #5
    'I appreciated that you came to our meeting yesterday.':
    '어제 우리 모임에 와 주어서 고마워.',
    #6
    'I appreciated that you came to our meeting yesterday.':
    '어제 저희 모임에 와 주시어서 고맙십니다.',
}

class Sentence (object):
    def __init__(self, **kwargs):
        self.raw_constituents = kwargs
        self.raw = self.raw_constituents
    def __eq__(self, other):
        return repr(self)==other
    def __repr__(self):
        sentence = ' '.join([
            self.raw['subject'] + self.raw['subject_particle'],
            self.raw['location'] + self.raw['location_particle'],
            self.raw['object'] + self.raw['object_particle'],
            self.raw['verb'],
        ])
        return sentence

class TestSentence(unittest.TestCase):
    def test1(self):
        self.assertEquals(
            Sentence(
                subject='앤드류',
                subject_particle='가',
                location='집',
                location_particle='에서',
                object='점심',
                object_particle='을',
                verb='머거요',
                ), 
            '앤드류가 집에서 점심을 머거요'
            )

if __name__ == '__main__': 
    unittest.main()