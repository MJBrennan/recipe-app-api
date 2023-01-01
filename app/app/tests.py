"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):

    def test_add_numbers(self):
        """ Tests adding numbners """
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_subtract_numbers(self):
         """ Test subtract numbners """
         res = calc.subtract(7, 6)

         self.assertEquals(res, 1)
