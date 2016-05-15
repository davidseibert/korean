from base import Base
from morphology import NomSuffix, AccSuffix, LocSuffix

class Dependency(Base):
    def __init__(self, head, dependent):
        self.head = head
        self.dependent = dependent
        self._setup()

    def spellout(self):
        text = self.dependent.spellout()
        return text

    def tree(self):
        return Tree(self.__class__.__name__, [self.dependent.tree()])

class Nsubj(Dependency):
    """subject"""
    def _setup(self):
        self.dependent.features['case'] = Nom()
class Dobj(Dependency):
    """direct object"""
    def _setup(self):
        self.dependent.features['case'] = Acc()
        pass
class Nmod(Dependency):
    """nominal modifier"""
    def _setup(self):
        pass
class Location(Dependency):
    """locative nominal modifier"""
    def _setup(self):
        self.dependent.features['case'] = Loc()
        pass

class Feature(object):
    pass
class InflectionalFeature(Feature):
    pass
class NominalInflectionalFeature(InflectionalFeature):
    pass
class Case(NominalInflectionalFeature):
    def apply(self, node):
        self.suffix.set_allomorph(node)
        node.suffixes.append(self.suffix)
class Nom(Case):
    suffix = NomSuffix()
    """nominative / direct: subject form of the noun"""


class Acc(Case):
    suffix = AccSuffix()
    """accusative / oblique: direct objects of verbs"""
class Loc(Case):
    suffix = LocSuffix()
    """locative: location in space or time"""

