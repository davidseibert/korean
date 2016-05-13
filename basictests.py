# coding: utf-8

import unittest
import lexicon
from syntax import Sentence
from morphology import Noun


class Experiment(object):
    def __init__(self, canon, hypo):
        self.canon = canon
        self.hypo = hypo
    def test(self, test_case):
        test_case.assertEquals(self.canon, str(self.hypo))

class TestSentences(unittest.TestCase):

    def test_verb_only(self):
        Experiment(
            '머거요',
             Sentence(
                 verb=lexicon.eat,
         )).test(self)

    def test_subject_verb(self):
        Experiment(
            '연정이 머거요',
            Sentence(
                subject=lexicon.emma,
                verb=lexicon.eat,
         )).test(self)

    def test_subject_object_verb(self):
        Experiment(
            '데이브가 점심을 머거요',
            Sentence(
                subject=lexicon.dave,
                object=lexicon.lunch,
                verb=lexicon.eat,
         )).test(self)

    def test_subject_location_object_verb(self):
        Experiment(
            '엘리가 집에서 트리트를 머거요',
            Sentence(
                subject=lexicon.elly,
                location=lexicon.house,
                object=lexicon.treat,
                verb=lexicon.eat,
         )).test(self)


if __name__ == '__main__': 
    unittest.main(verbosity=2)
