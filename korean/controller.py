# coding: utf-8

from syllable import break_word_into_syllables, Syllable

# build the words we need
class Word(object):
    pass   
class Verb(Word):
    pass
class Noun(Word):
    pass


class Dave(Noun):
    stem = u'데이브'
class Lunch(Noun):
    stem = u'점심'
class Emma(Noun):
    stem = u'연정'
class Elly(Noun):
    stem = u'엘리'
class Eat(Verb):
    stem = u'머거요'

emma = Emma()
elly = Elly()
dave = Dave()
lunch = Lunch()
eat_for_elly = Eat()
eat_for_emma = Eat()
eat_for_dave = Eat()

# apply semantic dependencies

eat_for_elly.agent = elly
eat_for_emma.agent = emma
eat_for_dave.agent = dave
eat_for_dave.patient = lunch

# apply syntactic dependencies

eat_for_elly.subject = eat_for_elly.agent
eat_for_emma.subject = eat_for_emma.agent

ds_elly = [eat_for_elly.subject, eat_for_elly]
ds_emma = [eat_for_emma.subject, eat_for_emma]

# apply morphosyntactic dependencies

def set_nom(ds):
    for i in ds:
        if hasattr(i, 'subject'):
            i.subject.case = 'Nom'


eat_for_elly.subject.case = 'Nom'
set_nom(ds_elly)
eat_for_emma.subject.case = 'Nom'
set_nom(ds_emma)


# resolve morphophonemic features

allomorphs = (u'이', u'가')

def has_tail(word):
    if word.syllables[-1].has_tail():
        return True
    else:
        return False
        
elly.syllables = break_word_into_syllables(elly)
emma.syllables = break_word_into_syllables(emma)
eat_for_elly.syllables = break_word_into_syllables(eat_for_elly)
eat_for_emma.syllables = break_word_into_syllables(eat_for_emma)

if has_tail(elly):
    elly.syllables.append(Syllable(allomorphs[0]))
else:
    elly.syllables.append(Syllable(allomorphs[1]))
    
if has_tail(emma):
    emma.syllables.append(Syllable(allomorphs[0]))
else:
    emma.syllables.append(Syllable(allomorphs[1]))
            
# flatten

def flatten_word(word):
    text = ''.join([s.spellout() for s in word.syllables])
    return text

def flatten_clause(words):
    text = ' '.join(flatten_word(w) for w in words)
    return text


s1 = flatten_clause([elly, eat_for_elly])
s2 = flatten_clause([emma, eat_for_emma])

print s1
print s2

def main():
    pass
    
if __name__ == '__main__':
    main()