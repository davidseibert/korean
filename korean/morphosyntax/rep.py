# coding: utf-8

class MorphosyntacticRepresentation(object):
    cases = {
                'subject': 'Nom',
                'object': 'Acc',
                'at': 'Loc',
            }
    def __init__(self, syntactic_representation):
        self.words = syntactic_representation.words
        self.set_cases()

    def set_case(self, word, case):
        word.case = case

    def set_cases(self):
        for word in self.words:
            for role, case in self.cases.iteritems():
                if hasattr(word, role) and getattr(word, role):
                    self.set_case(getattr(word, role), self.cases[role])

    def export(self):
        return self

    def debug(self):
        print self.words



