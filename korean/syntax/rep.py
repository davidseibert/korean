# coding: utf-8

class SyntacticRepresentation(object):
    def __init__(self, semantic_representation):
        self.verb = semantic_representation.verb
        self.verb.subject = self.verb.agent
        self.verb.object = self.verb.patient
        self.make_word_list()

    def make_word_list(self):
        self.words = [i for i in [
                self.verb.subject,
                self.verb.object,
                self.verb.at,
                self.verb,
                ] if i]

    def export(self):
        return self.words
