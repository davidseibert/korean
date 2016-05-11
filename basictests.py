# coding: utf-8

import unittest
from model import Sentence

example_verb_only = (
    '머거요',
     Sentence(
        verb='머거요',
        ).flatten()
)

example_subject_verb = (
    '데이브가 머거요',
     Sentence(
        subject='데이브',
        subject_particle='가',
        verb='머거요',
        ).flatten()
)

example_subject_object_verb = (
    '데이브가 점심을 머거요',
     Sentence(
        subject='데이브',
        subject_particle='가',
        object='점심',
        object_particle='을',
        verb='머거요',
        ).flatten()
)

example_subject_location_object_verb = (
    '데이브가 집에서 점심을 머거요',
     Sentence(
        subject='데이브',
        subject_particle='가',
        location='집',
        location_particle='에서',
        object='점심',
        object_particle='을',
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
    unittest.main()