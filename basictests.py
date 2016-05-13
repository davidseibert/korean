# coding: utf-8

import unittest
from syntax import Sentence

example_verb_only = (
    '머거요',
     Sentence(
        verb='머거요',
        ).flatten()
)

example_subject_verb = (
    '연정이 머거요',
     Sentence(
        subject='연정',
        verb='머거요',
        ).flatten()
)

example_subject_object_verb = (
    '데이브가 점심을 머거요',
     Sentence(
        subject='데이브',
        object='점심',
        verb='머거요',
        ).flatten()
)

example_subject_location_object_verb = (
    '엘리가 집에서 트리트를 머거요',
     Sentence(
        subject='엘리',
        location='집',
        object='트리트',
        verb='머거요',
        ).flatten()
)

class TestSentence(unittest.TestCase):
    def test_verb_only(self):
        self.assertEquals(*example_verb_only)
    def test_subject_verb(self):
        self.assertEquals(*example_subject_verb)
    def test_subject_object_verb(self):
        self.assertEquals(*example_subject_object_verb)
    def test_subject_location_object_verb(self):
        self.assertEquals(*example_subject_location_object_verb)

if __name__ == '__main__': 
    unittest.main(verbosity=2)