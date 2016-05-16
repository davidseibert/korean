# coding: utf-8

import unittest
from korean.utils.spellout_test import SpelloutTest
from korean.production import Production
from korean.lexicon import Dave, Lunch, Emma, Elly, Eat, Treat, House

# Test-specific Imports

class TestSentences(SpelloutTest):

    def test_verb_only(self):
        self.check(
            u'머거요',
            Production(Eat())
        )

    def test_subject_verb(self):
        self.check(
            u'연정이 머거요',
            Production(Eat(), Emma())
        )

    def test_subject_object_verb(self):
        self.check(
            u'데이브가 점심을 머거요',
            Production(Eat(), Dave(), Lunch())
        )

    def test_subject_location_object_verb(self):
        self.check(
            u'엘리가 트리트를 집에서 머거요',
            Production(Eat(), Elly(), Treat(), House())
        )

def test():
    unittest.main(verbosity=2)

if __name__ == '__main__':
    test()
