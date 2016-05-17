# coding: utf-8

class MorphosyntacticRepresentation(object):
    cases = {
                'subject': 'Nom',
                'object': 'Acc',
                'at': 'Loc',
            }
    def __init__(self, words):
        self._words = words
        self._set_cases()

    def _set_cases(self):
        for word in self._words:
            for role, case in self.cases.iteritems():
                try:
                    getattr(word, role).case = self.cases[role]
                except AttributeError:
                    continue

    def export(self):
        return self._words
