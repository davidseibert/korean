# coding: utf-8

class SemanticRepresentation(object):
    def __init__(self, verb, agent=None, patient=None, at=None):
        self.verb = verb
        self.verb.agent = agent
        self.verb.patient = patient
        self.verb.at = at

    def export(self):
        return self
