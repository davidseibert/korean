from tree import Tree
from StringIO import StringIO
import sys
from copy import copy

class Base(object):

    def ascii(self):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        self.tree().pretty_print(ansi=True, unicodelines=True, funccolor='yellow', nodecolor='blue', leafcolor='red')
        sys.stdout = old_stdout
        return result.getvalue().replace('-', '')

    def copy(self):
        return copy(self)

    def print_all(self):
        print self
        print
        print self.ascii()


