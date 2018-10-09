import unittest
#failing test
from cp2c import *

#successful test
#from cp3c import * 

class test_cleansing (unittest.TestCase):

    def setUp(self):
        self.d = dc("f500s")
        self.dd = dc("f500e")

    def test_name(self):
        self.assertEqual(self.d.name, "f500s")
        self.assertEqual(self.dd.name, "f500e")

    def test_get_filename(self):
        self.assertEqual(self.d.get_filename(), "f500s.csv")
        self.assertEqual(self.dd.get_filename(), "f500e.csv")

    def test_file_ok(self):
        self.assertEqual(self.d.file_ok(), True)
        self.assertEqual(self.dd.file_ok(), False)

    def test_len(self):
        self.assertEqual(self.d.len(), 16)
        self.assertEqual(self.dd.len(), 16)

    def test_len_clean(self):
        self.assertEqual(self.d.len_clean(), 16)
        self.assertEqual(self.dd.len_clean(), 14)

    def test_out_msg(self):
        self.assertEqual(self.d.out_msg(), "All profits are numeric. No changes in length and data types:"
)
        self.assertEqual(self.dd.out_msg(), "non-numeric profits are removed. New length and data types:"
)

suite = unittest.TestLoader().loadTestsFromTestCase(test_cleansing)
unittest.TextTestRunner(verbosity=2).run(suite)
