from base import Base, Tree
from dependencies import Nsubj, Dobj, Location
import phonology

class Node(Base):
    def __init__(self, **kwargs):
        self.complements = []
        self.adjuncts = []
        self.features = {}
        self.suffixes = []
        self.parse(**kwargs)

    def analyze(self):
        self.syllables = [phonology.Syllable(i) for i in self.stem.input]
        for suffix in self.suffixes:
            self.syllables += suffix.syllables

    def inflect(self):
        pass

    def has_tail(self):
        if self.stem.syllables[-1].has_tail():
            return True
        else:
            return False

    def spellout(self):
        self.analyze()
        self.inflect()
        stem_text = self.stem.spellout()
        suffixes_text = ''.join([i.spellout() for i in self.suffixes])
        obj_parts = self.complements + self.adjuncts
        text_parts = [i.spellout() for i in obj_parts]
        text_parts.append(stem_text + suffixes_text)
        text = ' '.join(text_parts)
        return text

    def parse(self, **kwargs):
        pass

    def tree(self):
        return Tree(self.__class__.__name__, [self.spellout()])
    
class Verb(Node):
    """Verb"""
    pass
    
class TransitiveVerb(Verb):
    """Transitive Verb"""
    
    def parse(self, subject=None, object=None, **adjuncts):
        self.parse_complements(subject, object)
        self.parse_adjuncts(**adjuncts)

    def parse_complements(self, subject, object):
        self.set_subject(subject)
        self.set_object(object)

    def parse_adjuncts(self, **adjuncts):
        for attr, Node in adjuncts.iteritems():
            getattr(Node, 'set_' + attr)(self)

    def set_subject(self, node):
        if node:
            self.complements.append(Nsubj(self, node))
    def set_object(self, node):
        if node:
            self.complements.append(Dobj(self, node))

    def tree(self):
        dependencies = self.complements + self.adjuncts
        dep_style_tree = Tree('-' + self.spellout(), [i.tree() for i in dependencies])
        node_style_tree = Tree(self.__class__.__name__, [dep_style_tree])
        return node_style_tree

class Noun(Node):
    """Noun"""
    def inflect(self):
        try:
            case = self.features['case']
        except KeyError:
            pass
        else:
            case.apply(self)


class Place(Noun):
    """Place Noun"""
    def parse(self):
        pass

    def set_at(self, node):
        if node:
            node.adjuncts.append(Location(node, self))
        return node

class Propn(Noun):
    """Proper Noun"""
    pass


