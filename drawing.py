import treeprettyprinter
from nltk.tree import Tree

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

sentence.pretty_print(ansi=True, unicodelines=True, nodecolor='red', leafcolor='blue')
