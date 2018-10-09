import unittest
#failing test
#from cp1c import *

#successful test
from cp2c import *

class test_cleansing (unittest.TestCase):

    def setUp(self):
        self.d = dc("f500s")
        self.dd = dc("f500e")

    def test_name(self):
        self.assertEqual(self.d.name, "f500s")

    def test_get_filename(self):
        self.assertEqual(self.d.get_filename(), "f500s.csv")

    def test_file_ok(self):
        self.assertEqual(self.d.file_ok(), True)
        self.assertEqual(self.dd.file_ok(), False)

suite = unittest.TestLoader().loadTestsFromTestCase(test_cleansing)
unittest.TextTestRunner(verbosity=2).run(suite)
