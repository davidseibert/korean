# coding: utf-8

class SyntacticRepresentation(object):
    def __init__(self, semantic_representation):
        self.verb = semantic_representation.verb
        self.link()
        self.make_word_list()

    def link(self):
        self.verb.subject = self.verb.agent
        self.verb.object = self.verb.patient

    def make_word_list(self):
        words = []
        if self.verb.subject:
            words.append(self.verb.subject)
        if self.verb.object:
            words.append(self.verb.object)
        if self.verb.at:
            words.append(self.verb.at)
        words.append(self.verb)
        self.words = words

    def export(self):
        return self

    def debug(self):
        print "Verb: {}".format(self.verb)
        print "Subject: {}".format(self.verb.subject)
        print "Object: {}".format(self.verb.object)


