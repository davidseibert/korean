# coding: utf-8

import unittest
from utils.spellout import SpelloutTest

from lexicon import Eat, Emma, Elly, Dave, Lunch, House, Treat

class TestSentences(SpelloutTest):

    def test_verb_only(self):
        self.check(
            u'머거요',
            Eat(subject=None, object=None)
        )

    def test_subject_verb(self):
        self.check(
            u'연정이 머거요',
            Eat(subject=Emma(), object=None)
        )

    def test_subject_object_verb(self):
        self.check(
            u'데이브가 점심을 머거요',
            Eat(subject=Dave(), object=Lunch())
        )

    def test_subject_location_object_verb(self):
        self.check(
            u'엘리가 트리트를 집에서 머거요',
            Eat(subject=Elly(), object=Treat(), at=House())
        )



def test():
    #unittest.main(verbosity=2)
    print Eat(subject=Elly(), object=Treat(), at=House()).ascii()

if __name__ == '__main__':
    test()
