# coding: utf-8

"""
Core dependents of clausal predicates
=====================================

Nominal dep     Predicate dep   Misc
-----------     -------------   ----

nsubj           csubj
nsubjpass       csubjpass
dobj            ccomp           xcomp
iobj

Noun dependents
===============

Nominal dep     Predicate dep   Modifier word
-----------     -------------   -------------

nummod          acl             amod
appos                           det
nmod                            neg

Case-marking, prepositions, possessive
======================================

case

Non-core dependents of clausal predicates
=========================================

Nominal dep     Predicate dep   Modifier word
-----------     -------------   -------------

nmod            advcl           advmod
                                neg

Compounding and unanalyzed
==========================

compound        mwe             goeswith
name            foreign

Loose joining relations
=======================

list            parataxis       remnant
dislocated                      reparandum

Special clausal dependents
==========================

Nominal dep     Auxiliary   Other
-----------     ---------   -----

vocative        aux         mark
discourse       auxpass     punct
expl            cop

Coordination
============

conj            cc              punct

Other
=====

Sentence head   Unspecified dependency
-------------   ----------------------

root            dep

"""

class Dependency(object):
    pass

class Acl(Dependency):
    """clausal modifier of noun (adjectival clause)

    acl stands for finite and non-finite clauses that modify a nominal. The acl relation contrasts with the advcl relation, which is used for adverbial clauses that modify a predicate. The head of the acl relation is the noun that is modified, and the dependent is the head of the clause that modifies the noun."""
    pass
class Advcl(Dependency):
    """adverbial clause modifier

    An adverbial clause modifier is a clause which modifies a verb or other predicate (adjective, etc.), as a modifier not as a core complement. This includes things such as a temporal clause, consequence, conditional clause, purpose clause, etc. The dependent must be clausal (or else it is an advmod) and the dependent is the main predicate of the clause."""
    pass
class Advmod(Dependency):
    """adverbial modifier

    An adverbial modifier of a word is a (non-clausal) adverb or adverbial phrase that serves to modify the meaning of the word.

    Note that in some grammatical traditions, the term adverbial modifier covers constituents that function like adverbs regardless whether they are realized by adverbs, adpositional phrases, or nouns in particular morphological cases. We differentiate adverbials realized as adverbs (advmod) and adverbials realized by noun phrases or adpositional phrases (nmod)."""
    pass
class Amod(Dependency):
    """adjectival modifier

    An adjectival modifier of a noun is any adjectival phrase that serves to modify the meaning of the noun."""
    pass
class Appos(Dependency):
    """appositional modifier

    An appositional modifier of a noun is a nominal immediately following the first noun that serves to define or modify that noun. It includes parenthesized examples, as well as defining abbreviations in one of these structures."""
    pass
class Aux(Dependency):
    """auxiliary

    An auxiliary of a clause is a non-main verb of the clause, e.g., a modal auxiliary, or a form of be, do or have in a periphrastic tense.

    Exception: Auxiliary verb used to construct the passive voice is not labeled aux but auxpass."""
    pass
class Auxpass(Dependency):
    """passive auxiliary

    A passive auxiliary of a clause is a non-main verb of the clause which contains the passive information."""
    pass
class Case(Dependency):
    """case marking

    The case relation is used for any case-marking element which is treated as a separate syntactic word (including prepositions, postpositions, and clitic case markers). Case-marking elements are treated as dependents of the noun or clause they attach to or introduce. (Thus, contrary to SD, UD abandons treating a preposition as a mediator between a modified word and its object.) The case relation aims at providing a more uniform analysis of nominal elements, prepositions and case in morphologically rich languages: a nominal in an oblique case will receive the same dependency structure as a nominal introduced by an adposition."""
    pass
class Cc(Dependency):
    """coordinating conjunction

    For more on coordination, see the conj relation. A cc is the relation between the first conjunct and the coordinating conjunction delimiting another conjunct. (Note: different dependency grammars have different treatments of coordination. We take the first conjunct as the head of the coordination.)"""
    pass
class Ccomp(Dependency):
    """clausal complement

    A clausal complement of a verb or adjective is a dependent clause which is a core argument. That is, it functions like an object of the verb, or adjective."""
    pass
class Compound(Dependency):
    """compound

    compound is one of the three relations in UD for compounding.

    It is used for compound words, numbers, and particles of phrasal verbs"""
    pass
class Conj(Dependency):
    """conjunct

    A conjunct is the relation between two elements connected by a coordinating conjunction, such as and, or, etc. We treat conjunctions asymmetrically: The head of the relation is the first conjunct and all the other conjuncts depend on it via the conj relation."""
    pass
class Cop(Dependency):
    """copula

    A copula is the relation between the complement of a copular verb and the copular verb to be (only). (We normally take a copula as a dependent of its complement.)"""
    pass
class Csubj(Dependency):
    """clausal subject

    A clausal subject is a clausal syntactic subject of a clause, i.e., the subject is itself a clause. The governor of this relation might not always be a verb: when the verb is a copular verb, the root of the clause is the complement of the copular verb. The dependent is the main lexical verb or other predicate of the subject clause. In the following example, what she said (that is, said is the clausal subject of makes."""
    pass
class Csubjpass(Dependency):
    """clausal passive subject

    A clausal passive subject is a clausal syntactic subject of a passive clause (or more generally, any voice where the proto-agent argument does not become the subject of the clause). In the example below, that she lied is the subject."""
    pass
class Dep(Dependency):
    """unspecified dependency

    A dependency is labeled as dep when a system is unable to determine a more precise dependency relation between two words. This may be because of a weird grammatical construction, a limitation in software (e.g. the Stanford Dependency conversion), a parser error, or because of an unresolved long distance dependency."""
    pass
class Det(Dependency):
    """determiner

    The relation determiner (det) holds between a nominal head and its determiner. Most commonly, a word of POS DET will have the relation det and vice versa. The known exceptions at present are:

    In some of the datasets, a possessive determiner like [en] my is currently given the POS tag DET but the relation nmod, so that it is parallel with other possessive constructions. This is not yet completely parallel across languages; in some languages, it is much more clear than in English how possessive determiners relate to adjectives, and the nmod relation is out of question."""
    pass
class Discourse(Dependency):
    """discourse element

    This is used for interjections and other discourse particles and elements (which are not clearly linked to the structure of the sentence, except in an expressive way). We generally follow the guidelines of what the Penn Treebanks count as an INTJ. They define this to include: interjections (oh, uh-huh, Welcome), fillers (um, ah), and discourse markers (well, like, actually, but not you know)."""
    pass
class Dislocated(Dependency):
    """dislocated elements

    The dislocated relation is used for fronted or postposed elements that do not fulfill the usual core grammatical relations of a sentence. These elements often appear to be in the periphery of the sentence, and may be separated off with a comma intonation."""
    pass
class Dobj(Dependency):
    """direct object

    The direct object of a verb is the second most core argument of a verb after the subject. Typically, it is the noun phrase that denotes the entity acted upon or which undergoes a change of state or motion (the proto-patient)."""
    pass
class Expl(Dependency):
    """expletive

    This relation captures expletive or pleonastic nominals. These are nominals that appear in an argument position of a predicate but which do not themselves satisfy any of the semantic roles of the predicate. The main predicate of the clause (the verb or predicate adjective or noun) is the governor. In English, this is the case for some uses of it and there: the existential there, and it when used in extraposition constructions. (Note that both it and there also have non-expletive uses.)"""
    pass
class Foreign(Dependency):
    """foreign words

    We use foreign to label sequences of foreign words. These are given a linear analysis: the head is the first token in the foreign phrase.

    foreign does not apply to loanwords or to foreign names. It applies to quoted foreign text incorporated in a sentence/discourse of the host language (unless we want to and know how to annotate the internal structure according to the syntax of the foreign language)."""
    pass
class Goeswith(Dependency):
    """goes with

    This relation links two parts of a word that are separated in text that is not well edited. The head is in some sense the “main” part, often the second part."""
    pass
class Iobj(Dependency):
    """indirect object

    The indirect object of a verb is any nominal phrase that is a core argument of the verb but is not its subject or direct object."""
    pass
class List(Dependency):
    """list

    The list relation is used for chains of comparable items. In lists with more than two items, all items of the list should modify the first one. Informal and web text often contains passages which are meant to be interpreted as lists but are parsed as single sentences. Email signatures often contain these structures, in the form of contact information: the different contact information items are labeled as list; the key-value pair relations are labeled as appos."""
    pass
class Mark(Dependency):
    """marker

    A marker is the word introducing a finite clause subordinate to another clause. For a complement clause, this is words like [en] that or whether. For an adverbial clause, the marker is typically a subordinating conjunction like [en] while or although. The mark is a dependent of the subordinate clause head. In a relative clause, it is a normally uninflected word, which simply introduces a relative clause, such as [he] še. (In this last use, one needs to distinguish between relative clause markers, which are mark from relative pronouns, which fill a regular verbal argument or modifier grammatical relation."""
    pass
class Mwe(Dependency):
    """multi-word expression

    The multi-word expression (modifier) relation is one of the three relations (compound, mwe, name) for compounding. It is used for certain fixed grammaticized expressions that behave like function words or short adverbials.

    The scope of mwe annotation corresponds roughly to the fixed expressions category of Sag et al., but excludes any relations in scope of name or compound. Additionally, limited morphosyntactic variation may be allowed for MWEs in exceptional cases."""
    pass
class Name(Dependency):
    """name

    name is one of the three relations for compounding in UD (together with compound and mwe). It is used for proper nouns constituted of multiple nominal elements. For example, name would be used between the words of Hillary Rodham Clinton, New York, or Carl XVI Gustaf but not to replace the usual relations in a phrasal or clausal name like The king of Sweden or the novels The Lord of the Rings and Captured By Aliens. Words joined by name should all be part of a minimal noun phrase; otherwise regular syntactic relations should be used. This is basically similar to the treatment of noun compounds with compound, except that in many cases parts of the name may be another nominal element such as an adjective (United Airlines)."""
    pass
class Neg(Dependency):
    """negation modifier

    The negation modifier is the relation between a negation word and the word it modifies.

    Modifiers labeled neg depend either on a noun (group “noun dependents”) or on a predicate (group “non-core dependents of clausal predicates”)."""
    pass
class Nmod(Dependency):
    """nominal modifier

    The nmod relation is used for nominal modifiers. They depend either on another noun (group “noun dependents”) or on a predicate (group “non-core dependents of clausal predicates”).

    nmod is a noun (or noun phrase) functioning as a non-core (oblique) argument or adjunct. This means that it functionally corresponds to an adverbial when it attaches to a verb, adjective or other adverb. But when attaching to a noun, it corresponds to an attribute, or genitive complement (the terms are less standardized here)."""
    pass
class Nsubj(Dependency):
    """nominal subject

    A nominal subject (nsubj) is a nominal phrase which is the syntactic subject and the proto-agent of a clause. That is, it is in the position that passes typical grammatical test for subjecthood, and this argument is the more agentive, the do-er, or the proto-agent of the clause. (See csubj for when the subject is clausal. See nsubjpass and csubjpass for when the subject is not the proto-agent argument due to valence changing operations. The nsubj role is only applied to semantic arguments of a predicate. When there is an empty argument in a grammatical subject position, it is labeled as expl. If there is then a displaced subject in the clause, as in the English existential there construction, it will be labeled as nsubj.) The governor of the nsubj relation might not always be a verb: when the verb is a copular verb, the root of the clause is the complement of the copular verb, which can be an adjective or noun."""
    pass
class Nsubjpass(Dependency):
    """passive nominal subject

    A passive nominal subject is a noun phrase which is the syntactic subject of a passive clause (or more generally, any voice where the proto-agent argument does not become the subject of the clause)."""
    pass
class Nummod(Dependency):
    """numeric modifier

    A numeric modifier of a noun is any number phrase that serves to modify the meaning of the noun with a quantity."""
    pass
class Parataxis(Dependency):
    """parataxis

    The parataxis relation (from Greek for “place side by side”) is a relation between a word (often the main predicate of a sentence) and other elements, such as a sentential parenthetical or a clause after a “:” or a “;”, placed side by side without any explicit coordination, subordination, or argument relation with the head word. Parataxis is a discourse-like equivalent of coordination, and so usually obeys an iconic ordering. Hence it is normal for the first part of a sentence to be the head and the second part to be the parataxis dependent, regardless of the headedness properties of the language. But things do get more complicated, such as cases of parentheticals, which appear medially."""
    pass
class Punct(Dependency):
    """punctuation

    This is used for any piece of punctuation in a clause, if punctuation is being retained in the typed dependencies."""
    pass
class Remnant(Dependency):
    """remnant in ellipsis

    The remnant relation is used to provide a satisfactory treatment of ellipsis (in the case of gapping and stripping, where a predicational or verbal head gets elided). This is something that was lacking in earlier versions of SD and provides a basis for being able to reconstruct dependencies in the enhanced representation of UD. In particular, the goal was to achieve this without having to postulate empty nodes in the basic representation."""
    pass
class Reparandum(Dependency):
    """overridden disfluency

    We use reparandum to indicate disfluencies overridden in a speech repair. The disfluency is the dependent of the repair."""
    pass
class Root(Dependency):
    """root

    The root grammatical relation points to the root of the sentence. A fake node ROOT is used as the governor. The ROOT node is indexed with 0, since the indexing of real words in the sentence starts at 1."""
    pass
class Vocative(Dependency):
    """vocative

    The vocative relation is used to mark dialogue participant addressed in text (common in conversations, emails and newsgroup postings). The relation links the addressee’s name to its host sentence."""
    pass
class Xcomp(Dependency):
    """open clausal complement

    An open clausal complement (xcomp) of a verb or an adjective is a predicative or clausal complement without its own subject. The reference of the subject is necessarily determined by an argument external to the xcomp (normally by the object of the next higher clause, if there is one, or else by the subject of the next higher clause). This is often referred to as obligatory control. These clauses tend to be non-finite in many languages, but they can be finite as well. The name xcomp is borrowed from Lexical-Functional Grammar."""
