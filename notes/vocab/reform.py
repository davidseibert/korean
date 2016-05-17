# coding 'utf-8'

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

from datetime import datetime

class Card(object):
    def __init__(self, rank, quotient, age, question, answer):
        self.rank = rank
        self.quotient = quotient
        self.age = age
        self.question = question.encode('utf-8')
        self.answer = answer

    @property
    def age_repr(self):
        seconds = self.age.seconds
        hours, remainder = divmod(seconds, 3600)
        minutes, remainder = divmod(hours, 60)
        hours_repr = str(hours) + 'h'
        minutes_repr = str(minutes) + 'm'
        return hours_repr + ' ' + minutes_repr

    def __repr__(self):
        format_string = '{0.rank}. {0.question} : {0.answer} ({0.age_repr}) [{0.quotient}]'
        return format_string.format(self)

class Deck(object):
    def __init__(self):
        self.cards = []

class Collection(object):
    def __init__(self, sourcefile_path):
        self.sourcefile_path = sourcefile_path
        self.read_raw_cards()
        self.cards = []

    def read_raw_cards(self):
        try:
            with open(self.sourcefile_path) as sourcefile:
                while True:
                    raw_card = next(sourcefile)
                    self.process_raw_card(raw_card)
        except StopIteration:
            print 'Done!'

    def add_card(self, card):
        self.cards.append(card)

    def process_raw_card(self, raw_card):
        unicode_card = raw_card.decode('utf-8')
        stripped = unicode_card.strip()
        fields = stripped.split('\t')
        rank, quotient, last_reviewed, question, answer = tuple(fields)
        last_reviewed_obj = datetime.strptime(last_reviewed, DATE_FORMAT)
        now = datetime.now()
        age = now - last_reviewed_obj
        card = Card(rank, quotient, age, question, answer)
        print repr(card)

class Coach(object):
    def __init__(self):
        self.collections = []

class Session(object):
    def __init__(self):
        pass
    
    def get_date(self):
        now = datetime.now()
        print now.strftime(DATE_FORMAT)



def main():
    top10 = Collection('top10.tsv')

if __name__ == '__main__':
    main()

    

