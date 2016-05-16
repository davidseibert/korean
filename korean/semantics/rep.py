# coding: utf-8

class SemanticRepresentation(object):
    def __init__(self, verb, agent=None, patient=None, at=None):
        self.verb = verb
        self.agent = agent
        self.patient = patient
        self.at = at
        self.link()

    def link(self):
        self.verb.agent = self.agent
        self.verb.patient = self.patient
        self.verb.at = self.at

    def export(self):
        return self

    def debug(self):
        print "Verb: {}".format(self.verb)
        print "Agent: {}".format(self.agent)
        print "Patient: {}".format(self.patient)


