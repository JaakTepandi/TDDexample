import unittest

#failing test
from cp0c import cp

#successful test
#from cp1c import cp

class test_cleansing (unittest.TestCase):

    def test_t1(self):
        self.assertEqual(cp("fortune500"), "removed")


suite = unittest.TestLoader().loadTestsFromTestCase(test_cleansing)
unittest.TextTestRunner(verbosity=2).run(suite)
