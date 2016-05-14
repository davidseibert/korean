# coding: utf-8

# Base Classes
class Feature(object):
    pass
class LexicalFeature(Feature):
    pass
class InflectionalFeature(Feature):
    pass
class NominalInflectionalFeature(InflectionalFeature):
    pass
class VerbalInflectionalFeature(InflectionalFeature):
    pass

# Pronoun Types
class PronType(LexicalFeature):
    pass
class Prs(PronType): 
    """personal or possessive personal pronoun or determiner"""
    pass
class Rcp(PronType): 
    """reciprocal pronoun"""
    pass
class Art(PronType): 
    """article"""
    pass
class Int(PronType): 
    """interrogative pronoun, determiner, numeral or adverb"""
    pass
class Rel(PronType): 
    """relative pronoun, determiner, numeral or adverb"""
    pass
class Dem(PronType): 
    """demonstrative pronoun, determiner, numeral or adverb"""
    pass
class Tot(PronType): 
    """total (collective) pronoun, determiner or adverb"""
    pass
class Neg(PronType): 
    """negative pronoun, determiner or adverb"""
    pass
class Ind(PronType): 
    """indefinite pronoun, determiner, numeral or adverb"""
    pass

# Number Types
class NumType(LexicalFeature):
    pass
class Card(NumType): 
    """cardinal number or corresponding interrogative / relative / indefinite / demonstrative word"""
    pass
class Ord(NumType): 
    """ordinal number or corresponding interrogative / relative / indefinite / demonstrative word"""
    pass
class Mult(NumType): 
    """multiplicative numeral or corresponding interrogative / relative / indefinite / demonstrative word: 'once', 'twice', etc."""
    pass
class Frac(NumType): 
    """fraction"""
    pass
class Sets(NumType): 
    """number of sets of things"""
    pass
class Dist(NumType): 
    """distributive numeral: the same quantity distributed to each member in a set"""
    pass
class Range(NumType): 
    """range of values"""
    pass
class Gen(NumType): 
    """generic numeral, i.e. a numeral that is neither of the above"""
    pass

# Possessive
class Poss(LexicalFeature):
    pass

# Reflexive
class Reflex(LexicalFeature):
    pass

# Genders
class Gender(NominalInflectionalFeature):
    pass
class Masc(Gender): 
    """masculine gender"""
    pass
class Fem(Gender): 
    """feminine gender"""
    pass
class Neut(Gender): 
    """neuter gender"""
    pass
class Com(Gender): 
    """common gender (not neuter)"""
    pass

# Animacy
class Animacy(NominalInflectionalFeature):
    pass

class Anim(Animacy): 
    """animate"""
    pass
class Nhum(Animacy): 
    """animate but non-human"""
    pass
class Inan(Animacy): 
    """inanimate"""
    pass

# Number
class Number(NominalInflectionalFeature):
    pass
class Sing(Number): 
    """singular number"""
    pass
class Plur(Number): 
    """plural number"""
    pass
class Dual(Number): 
    """dual number"""
    pass
class Ptan(Number): 
    """plurale tantum"""
    pass
class Coll(Number): 
    """collective / mass / singulare tantum"""
    pass

# Cases
class Case(NominalInflectionalFeature):
    pass
class Nom(Case): 
    """nominative / direct: subject form of the noun"""
    pass
class Acc(Case): 
    """accusative / oblique: direct objects of verbs"""
    pass
class Abs(Case): 
    """absolutive: subject of intransitive verb and direct object of transitive verb."""
    pass
class Erg(Case): 
    """ergative: subject of transitive verb."""
    pass
class Dat(Case): 
    """dative: indirect objects of verbs."""
    pass
class Gen(Case): 
    """genitive: 'of' its governor"""
    pass
class Voc(Case): 
    """vocative: used to address someone"""
    pass
class Loc(Case): 
    """locative: location in space or time"""
    pass
class Ins(Case): 
    """instrumental / instructive: used as instrument to do something """
    pass
class Par(Case): 
    """partitive: indefinite identity and unfinished actions without result"""
    pass
class Dis(Case): 
    """distributive: something happened to every member of a set, one in a time, or frequency."""
    pass
class Ess(Case): 
    """essive / prolative: The essive case expresses a temporary state, 'as a'"""
    pass
class Tra(Case): 
    """translative / factive: change of state, 'becomes' """
    pass
class Com(Case): 
    """comitative / associative: 'together with'"""
    pass
class Abe(Case): 
    """abessive: 'without'"""
    pass
class Ine(Case): 
    """inessive: location inside of something."""
    pass
class Ill(Case): 
    """illative: direction into something"""
    pass
class Ela(Case): 
    """elative: direction out of something"""
    pass
class Add(Case): 
    """additive: ???"""
    pass
class Ade(Case): 
    """adessive: location at or on something"""
    pass
class All(Case): 
    """allative: direction to something """
    pass
class Abl(Case): 
    """ablative: direction from some point."""
    pass
class Sup(Case): 
    """superessive: location on top of something or on the surface of something"""
    pass
class Sub(Case): 
    """sublative: destination of movement"""
    pass
class Del(Case): 
    """delative: movement from the surface of something"""
    pass
class Lat(Case): 
    """lative / directional allative: movement towards/to/into/onto something"""
    pass
class Tem(Case): 
    """temporal: indicates time"""
    pass
class Ter(Case): 
    """terminative / terminal allative: where something ends in space or time"""
    pass
class Cau(Case): 
    """causative / motivative: the cause or goal of something"""
    pass
class Ben(Case): 
    """benefactive / destinative: 'for'"""
    pass

# Definiteness
class Definite(NominalInflectionalFeature):
    pass
class Ind(Definite): 
    """indefinite"""
    pass
class Def(Definite): 
    """definite"""
    pass
class Red(Definite): 
    """reduced ??"""
    pass
class Com(Definite): 
    """complex ??"""
    pass

# Degrees
class Degree(NominalInflectionalFeature):
    pass
class Pos(Degree): 
    """positive, first degree"""
    pass
class Cmp(Degree): 
    """comparative, second degree"""
    pass
class Sup(Degree): 
    """superlative, third degree"""
    pass
class Abs(Degree): 
    """absolute superlative"""
    pass

# Negative
class Negative(NominalInflectionalFeature):
    pass
class Pos(Negative): 
    """positive, affirmative"""
    pass
class Neg(Negative): 
    """negative"""
    pass

# Verb Forms
class VerbForm(VerbalInflectionalFeature):
    pass
class Fin(VerbForm): 
    """finite verb"""
    pass
class Inf(VerbForm): 
    """infinitive"""
    pass
class Sup(VerbForm): 
    """supine"""
    pass
class Part(VerbForm): 
    """participle"""
    pass
class Trans(VerbForm): 
    """transgressive"""
    pass
class Ger(VerbForm): 
    """gerund"""
    pass

# Moods
class Mood(VerbalInflectionalFeature):
    pass
class Ind(Mood): 
    """indicative:"""
    pass
class Imp(Mood): 
    """imperative:"""
    pass
class Cnd(Mood): 
    """conditional:"""
    pass
class Pot(Mood): 
    """potential: likely but not certain"""
    pass
class Sub(Mood): 
    """subjunctive / conjunctive: subjective or otherwise uncertain"""
    pass
class Jus(Mood): 
    """jussive: desire that the action happens"""
    pass
class Qot(Mood): 
    """quotative: denotes direct speech."""
    pass
class Opt(Mood): 
    """optative: 'may you ... !'"""
    pass
class Des(Mood): 
    """desiderative: 'want'"""
    pass
class Nec(Mood): 
    """necessitative: 'must'"""
    pass


# Tenses
class Tense(VerbalInflectionalFeature):
    pass
class Past(Tense): 
    """past tense / preterite / aorist"""
    pass
class Pres(Tense): 
    """present tense"""
    pass
class Fut(Tense): 
    """future tense"""
    pass
class Imp(Tense): 
    """imperfect"""
    pass
class Nar(Tense): 
    """narrative"""
    pass
class Pqp(Tense): 
    """pluperfect"""
    pass

# Aspects
class Aspect(VerbalInflectionalFeature):
    pass
class Imp(Aspect): 
    """imperfect aspect"""
    pass
class Perf(Aspect): 
    """perfect aspect"""
    pass
class Pro(Aspect): 
    """prospective aspect"""
    pass
class Prog(Aspect): 
    """progressive aspect"""
    pass

# Voices
class Voice(VerbalInflectionalFeature):
    pass
class Act(Voice): 
    """active voice"""
    pass
class Pass(Voice): 
    """passive voice"""
    pass
class Rcp(Voice): 
    """reciprocal voice"""
    pass
class Cau(Voice): 
    """causative voice"""
    pass

# Persons
class Person(VerbalInflectionalFeature):
    pass
class _1(Person): 
    """first person"""
    pass
class _2(Person): 
    """second person"""
    pass
class _3(Person): 
    """third person"""
    pass
