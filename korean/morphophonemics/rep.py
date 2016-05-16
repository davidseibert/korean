# coding: utf-8

from syllable import break_word_into_syllables, Syllable

class MorphophonemicRepresentation(object):
    nom_allomorphs = (u'이', u'가')
    acc_allomorphs = (u'을', u'를')
    case_morphemes = {
            'Nom': (u'이', u'가'),
            'Acc': (u'을', u'를'),
            'Loc': (u'에서'),
                }

    def __init__(self, morphosyntactic_representation):
        self.words = morphosyntactic_representation.words
        self.syllabify_words()
        self.add_suffixes_to_words()

    def export(self):
        return self

    def has_tail(self, word):
        if word.syllables[-1].has_tail():
            return True
        else:
            return False

    def syllabify_word(self, word):
        word.syllables = break_word_into_syllables(word)

    def syllabify_words(self):
        for word in self.words:
            self.syllabify_word(word)

    def add_nom_suffix(self, word):
        key = 'Nom'
        # check which allomorph to use
        if self.has_tail(word):
            word.syllables.append(Syllable(self.case_morphemes[key][0]))
        else:
            word.syllables.append(Syllable(self.case_morphemes[key][1]))

    def add_acc_suffix(self, word):
        key = 'Acc'
        # check which allomorph to use
        if self.has_tail(word):
            word.syllables.append(Syllable(self.case_morphemes[key][0]))
        else:
            word.syllables.append(Syllable(self.case_morphemes[key][1]))

    def add_loc_suffix(self, word):
        key = 'Loc'
        allomorph = self.case_morphemes[key]
        for i in allomorph:
            word.syllables.append(Syllable(i))

    def add_suffix_to_word(self, word):
        if hasattr(word, 'case'):
            if word.case == 'Nom':
                self.add_nom_suffix(word)
            if word.case == 'Acc':
                self.add_acc_suffix(word)
            if word.case == 'Loc':
                self.add_loc_suffix(word)

    def add_suffixes_to_words(self):
        for word in self.words:
            self.add_suffix_to_word(word)

    def flatten_word(self, word):
        text = ''.join([s.spellout() for s in word.syllables])
        return text

    def flatten_sentence(self):
        text = ' '.join(self.flatten_word(w) for w in self.words)
        return text
