#!/usr/bin/python3
""" base.py tests module """
import unittest
from models.base import Base
from unittest.mock import patch
from io import StringIO

class MyTestCase(unittest.TestCase):
    """ class for testcases """
    def test_0base(self):
        """ First test case """
        a = Base()
        self.assertEqual(a.id, 1)
    def test_1base(self):
        """ Second test case """
        a = Base()
        self.assertEqual(a.id, 2)
    def test_2base(self):
        """ Third test case """
        a = Base(14)
        self.assertEqual(a.id, 14)
    def test_3base(self):
        """ Fourth test case """
        a = Base()
        self.assertEqual(a.id, 3)

    def test_4base(self):
        """ Fifth test case """
        obj = Base.from_json_string('[{ "id": 89 }]')
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(type(obj))
            output = "<class 'list'>\n"
            self.assertEqual(fake_output.getvalue(), output)

    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(self.test_0base())
        suite.addTest(self.test_1base())
        suite.addTest(self.test_2base())
        suite.addTest(self.test_3base())
        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(MyTestClass().suite())
