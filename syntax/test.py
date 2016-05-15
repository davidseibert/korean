# coding: utf-8


from nodes import Propn, Place, Noun, TransitiveVerb



def test():
    emma = Propn(u'연정')
    elly = Propn(u'엘리')
    house = Place(u'집')
    treat = Noun(u'트리트')
    lunch = Noun(u'점심')
    eat = TransitiveVerb(u'머거요')

    s1 = eat(emma, lunch)
    s2 = house.at(eat(elly, treat))

    print s1.ascii()
    print s2.ascii()

def main():
    test()

if __name__ == '__main__': main()
