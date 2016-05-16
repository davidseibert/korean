# coding: utf-8

from semantics.rep import SemanticRepresentation
from syntax.rep import SyntacticRepresentation
from morphosyntax.rep import MorphosyntacticRepresentation
from morphophonemics.rep import MorphophonemicRepresentation

class Stage(object):
    def __init__(self, rep, export):
        self.rep = rep
        self.export = export

class Production(object):
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

        self.start()

    def start(self):
        self.semantics()
        self.syntax()
        self.morphosyntax()
        self.morphophonemics()
        self.spellout()

    def semantics(self):
        rep = SemanticRepresentation(*self.args, **self.kwargs)
        export = rep.export()
        self.sem = Stage(rep, export)

    def syntax(self):
        rep = SyntacticRepresentation(self.sem.export)        
        export = rep.export()
        self.syn = Stage(rep, export)

    def morphosyntax(self):
        rep = MorphosyntacticRepresentation(self.syn.export)        
        export = rep.export()
        self.mosyn = Stage(rep, export)

    def morphophonemics(self):
        rep = MorphophonemicRepresentation(self.mosyn.export)        
        export = rep.export()
        self.mopho = Stage(rep, export)

    def spellout(self):
        self.result = self.mopho.export.flatten_sentence()
        return self.result


def test():
    from lexicon import Dave, Lunch, Emma, Elly, Eat

    prod1 = Production(Eat(), Elly())
    prod2 = Production(Eat(), Emma())
    prod3 = Production(Eat(), Dave(), Lunch())

    print '*: ' + prod1.result
    print '*: ' + prod2.result
    print '*: ' + prod3.result


def main():
    test()
    
if __name__ == '__main__':
    main()
