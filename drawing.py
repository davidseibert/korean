import treeprettyprinter
from nltk.tree import Tree
from StringIO import StringIO
import sys
import pydoc

markets = Tree('markets', ['financial'])
economic = Tree('economic', [])
news = Tree('news', ['Economic'])
on = Tree('on', [markets])
effect = Tree('effect', ['little', on])
had = Tree('had', [news, effect])

#had.pretty_print(ansi=True, unicodelines=True)

def sbj(node):
    return Tree('-sbj', [node])
def obj(node):
    return Tree('-obj', [node])
def nmod(node):
    return Tree('-nmod', [node])
def pc(node):
    return Tree('-pc', [node])

markets = Tree('markets', [nmod('financial')])
news = Tree('news', [nmod('economic')])
on = Tree('on', [pc(markets)])
effect = Tree('effect', [nmod('little'), nmod(on)])
had = Tree('had', [sbj(news), obj(effect)])


sentence = had


old_stdout = sys.stdout

result = StringIO()

sys.stdout = result
sentence.pretty_print(ansi=True, unicodelines=True, nodecolor='red', leafcolor='blue')

sys.stdout = old_stdout

tree = result.getvalue()
tree = tree.encode('utf-8')
text = '... some text ... '
#pydoc.pager(tree * 10)
print tree * 10

