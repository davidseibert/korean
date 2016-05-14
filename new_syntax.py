# coding: utf-8

from nltk.tree import Tree
from StringIO import StringIO
import sys

def print_heading(text):
    print text
    print "=" * len(text)
    print

class Base(object):
    def __str__(self):
        return str(self.tree())

    def ascii(self):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        self.tree().pretty_print(ansi=True, unicodelines=True, nodecolor='red', leafcolor='blue')
        sys.stdout = old_stdout
        return result.getvalue()

    def print_all(self):
        print self
        print
        print self.ascii()


class Node(Base):
    def __init__(self, input):
        self.input = input

    def tree(self):
        return Tree(self.__class__.__name__, [self.input])
    
class Verb(Node):
    """Verb"""
    pass
    
class TransitiveVerb(Verb):
    """Transitive Verb"""
    
    def __call__(self, subject, object, loc=None):
        self.complements = [
                Nsubj(self, subject),
                Dobj(self, subject),
                ]
        return self
    def tree(self):
        dep_style_tree = Tree(self.input, [i.tree() for i in self.complements])
        node_style_tree = Tree(self.__class__.__name__, [dep_style_tree])
        return node_style_tree

class Noun(Node):
    """Noun"""
    pass

class Propn(Noun):
    """Proper Noun"""
    pass

class Dependency(Base):
    def __init__(self, head, dependent):
        self.head = head
        self.dependent = dependent

    def tree(self):
        return Tree(self.__class__.__name__, [self.dependent.tree()])

class Nsubj(Dependency):
    pass

class Dobj(Dependency):
    pass

dave = Propn(u'데이브')
elly = Propn(u'엘리')
house = Noun(u'집')
treat = Noun(u'트리트')


emma = Propn(u'연정')
lunch = Noun(u'점심')
eat = TransitiveVerb(u'머거요')

s = eat(emma, lunch)


test_emma = Propn('emma')
test_lunch = Noun('lunch')
test_eat = TransitiveVerb('eat')(test_emma, test_lunch)

test_nsubj1 = Nsubj(None, test_emma)
test_dobj1 = Dobj(None, test_lunch)

def tests():
    test_nodes()
    test_dependencies()
    model_tree()

def main():
    tests()

def test_dependencies():
    print_heading("Dependency Printing Tests")

    test_nsubj1.print_all()
    test_dobj1.print_all()

def test_nodes():
    print_heading("Node Printing Tests")

    test_emma.print_all()
    test_lunch.print_all()
    test_eat.print_all()

def model_tree():
    print "Complete Model Tree"
    print "==================="
    print

    tree = Tree('eat', 
            [
                Tree('Nsubj', ['emma']),
                Tree('Dobj', ['lunch']),
            ])

    print tree
    print
    tree.pretty_print(ansi=True, unicodelines=True, nodecolor='green', leafcolor='green')



if __name__ == '__main__': main()
