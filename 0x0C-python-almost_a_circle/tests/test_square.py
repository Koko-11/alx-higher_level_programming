#!/usr/bin/python3
""" module for square.py testing """
import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square

class Square_testing(unittest.TestCase):
    """ Test cases """
    def test_0square(self):
        """ First test case """
        s1 = Square(5, 0, 0, 43)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (43) 0/0 - 5\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "25\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "#####\n#####\n#####\n#####\n#####\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_1square(self):
        """ Second test case """
        s1 = Square(2, 2, 0, 85)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (85) 2/0 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "4\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "  ##\n  ##\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_2square(self):
        """ Third test case """
        s1 = Square(3, 1, 3, 71)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (71) 1/3 - 3\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.area())
            output = "9\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            s1.display()
            output = "\n\n\n ###\n ###\n ###\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_3square(self):
        """ Fourth test case """
        s1 = Square(5, 0, 0, 43)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (43) 0/0 - 5\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.size)
            output = "5\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.size = 10
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1.size)
            output = "10\n"
            self.assertEqual(fake_output.getvalue(), output)
        with self.assertRaises(TypeError):
            s1.size = "9"

    def test_4square(self):
        """ Fifth test case """
        s1 = Square(5, 0, 0, 38)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (38) 0/0 - 5\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(10)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (10) 0/0 - 5\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(1, 2)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (1) 0/0 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(1, 2, 3)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (1) 3/0 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(1, 2, 3, 4)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (1) 3/4 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(x=12)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (1) 12/4 - 2\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(size=7, y=1)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (1) 12/1 - 7\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1.update(size=7, id=89, y=1)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (89) 12/1 - 7\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_5square(self):
        """ Sixth test case """
        s1 = Square(10, 2, 1, 64)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1)
            output = "[Square] (64) 2/1 - 10\n"
            self.assertEqual(fake_output.getvalue(), output)
        s1_dictionary = s1.to_dictionary()
        s2 = Square(1, 1, 0, 90)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s2)
            output = "[Square] (90) 1/0 - 1\n"
            self.assertEqual(fake_output.getvalue(), output)
        s2.update(**s1_dictionary)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s2)
            output = "[Square] (64) 2/1 - 10\n"
            self.assertEqual(fake_output.getvalue(), output)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(s1 == s2)
            output = "False\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_6square(self):
        """ Sixth test case """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file(list_squares_input)
        list_squares_output = Square.load_from_file()
        self.assertNotEqual(list_squares_input, list_squares_output)
        for squr1, squr2 in zip(list_squares_input, list_squares_output):
            self.assertNotEqual(id(squr1), id(squr2))

    def test_7square(self):
        """ Seventh test case """
        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]
        Square.save_to_file_csv(list_squares_input)
        list_squares_output = Square.load_from_file_csv()
        self.assertNotEqual(list_squares_input, list_squares_output)
        for squr1, squr2 in zip(list_squares_input, list_squares_output):
            self.assertNotEqual(id(squr1), id(squr2))

    def test_8square(self):
        """ Eighth test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(Square(1))
            output = '[Square] (38) 0/0 - 1\n'
            self.assertEqual(fake_output.getvalue(),output)

    def test_9square(self):
        """ Nineth test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with self.assertRaises(TypeError):
                a = Square(1, "5")

    def test_10square(self):
        """ Tenth test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            with self.assertRaises(TypeError):
                a = Square(1, 5, "7")
