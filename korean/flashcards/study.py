# coding 'utf-8'
import signal
import sys

def exit_gracefully():
    sys.exit(0)

def signal_handler(signal, frame):
    print '\n\nCaught Ctrl-C'
    exit_gracefully()

signal.signal(signal.SIGINT, signal_handler)
from colorama import Fore, Back, Style

DATE_FORMAT = '%Y-%m-%d %H:%M:%S'

from datetime import datetime

class Card(object):
    def __init__(self, rank, quotient, last_reviewed, question, answer):
        self.rank = rank
        self.quotient = quotient
        self.last_reviewed = last_reviewed
        self.question = question.encode('utf-8')
        self.answer = answer

    def age(self):
        pass

    def age(self):
        pass

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
    
    def present(self):
        prompt_format = 'Q: {0.question}\nA: '
        prompt = prompt_format.format(self, Style)
        response = raw_input(prompt).decode('utf-8')
        self.check_response(response)

    def check_response(self, response):
        if response == self.answer:
            print "{0.GREEN}Good!{0.RESET}".format(Fore)
        else:
            print "{0.RED}No:{0.RESET} {1}".format(Fore, self.answer.encode('utf-8'))



class Deck(object):
    def __init__(self):
        self.cards = []

class Collection(object):
    def __init__(self, sourcefile_path):
        self.sourcefile_path = sourcefile_path
        self.cards = []
        self.read_raw_cards()

    def read_raw_cards(self):
        try:
            with open(self.sourcefile_path) as sourcefile:
                while True:
                    raw_card = next(sourcefile)
                    self.process_raw_card(raw_card)
        except StopIteration:
            pass

    def add_card(self, card):
        self.cards.append(card)

    def process_raw_card(self, raw_card):
        unicode_card = raw_card.decode('utf-8')
        stripped = unicode_card.strip()
        fields = stripped.split('\t')
        rank, quotient, last_reviewed, answer, question = tuple(fields)
        last_reviewed_obj = datetime.strptime(last_reviewed, DATE_FORMAT)
        now = datetime.now()
        age = now - last_reviewed_obj
        card = Card(rank, quotient, age, question, answer)
        self.add_card(card)

class Coach(object):
    def __init__(self):
        self.collections = []

class Session(object):
    def __init__(self, collection_name):
        self.collection = Collection('sets/' + collection_name + '.tsv')
    
    def get_date(self):
        now = datetime.now()
        print now.strftime(DATE_FORMAT)
        
    def start(self):
        try:
            for card in self.collection.cards:
                card.present()
        except KeyboardInterrupt:
            exit_gracefully()



def main():
    session = Session('top10')
    session.start()

if __name__ == '__main__':
    main()

    
