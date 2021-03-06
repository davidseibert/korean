import unittest

__unittest = True

class SpelloutTest(unittest.TestCase):
    def check(self, target, production):
        result = production.spellout()
        if target != result:
            msg="\nTarget: '{}'\nResult: '{}'".format(target.encode('utf-8'), result.encode('utf-8'))
            raise self.failureException(msg)

