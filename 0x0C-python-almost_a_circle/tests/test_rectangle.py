#!/usr/bin/python3
""" rectangle.py test module """
import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle
from models.base import Base
import os


class Test_rectangle(unittest.TestCase):
    """ Test cases for rectangle """
    def test_2rectangle(self):
        """ Third test case """
        r3 = Rectangle(10, 5)
        self.assertTupleEqual(
                (r3.width, r3.height, r3.x, r3.y),
                (10, 5, 0, 0)
                )

    def test_3rectangle(self):
        """ Fourth test case """
        r4 = Rectangle(10, 5, 3, 2)
        self.assertTupleEqual(
                (r4.width, r4.height, r4.x, r4.y),
                (10, 5, 3, 2)
                )

    def test_4rectangle(self):
        """ Fifth test case """
        r5 = Rectangle(10, 5, 3, 2, 22)
        self.assertTupleEqual(
                (r5.width, r5.height, r5.x, r5.y, r5.id),
                (10, 5, 3, 2, 22)
                )

    def test_5rectangle(self):
        """ sixth test case """
        with self.assertRaises(TypeError):
            r6 = Rectangle("2", 5)

    def test_6rectangle(self):
        """ Seventh test case """
        with self.assertRaises(TypeError):
            r7 = Rectangle(2, "5")

    def test_7rectangle(self):
        """ Eighth test case """
        with self.assertRaises(TypeError):
            r8 = Rectangle(2, 5, "3", 8)

    def test_8rectangle(self):
        """ Nineth test case """
        with self.assertRaises(TypeError):
            r9 = Rectangle(2, 5, 3, "8")

    def test_10rectangle(self):
        """ Tenth test case """
        with self.assertRaises(TypeError):
            r10 = Rectangle(2, 5, 3, [5])

    def test_11rectangle(self):
        """ 11th test case """
        with self.assertRaises(ValueError):
            r11 = Rectangle(0, 5, 3, 8)

    def test_12rectangle(self):
        """ 12th test case """
        with self.assertRaises(ValueError):
            r12 = Rectangle(2, 0, 3, 8)

    def test_rectangle12(self):
        """ Correction test case """
        with self.assertRaises(ValueError):
            r12c = Rectangle(-1, 3)

    def test_rectangle13(self):
        """ Correction test case """
        with self.assertRaises(ValueError):
            r13c = Rectangle(2, -6)

    def test_13rectangle(self):
        """ 13th test case """
        with self.assertRaises(ValueError):
            r13 = Rectangle(2, 5, -1, 8)

    def test_14rectangle(self):
        """ 14th test case """
        with self.assertRaises(ValueError):
            r14 = Rectangle(2, 5, 1, -8)

    def test_15rectangle(self):
        """ 15th test case """
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

    def test_16rectangle(self):
        """ 16th test case """
        r1 = Rectangle(2, 10)
        self.assertEqual(r1.area(), 20)

    def test_17rectangle(self):
        """ 17th test case """
        r1 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 56)

    def test_18rectangle(self):
        """ 18th test case """
        r1 = Rectangle(4, 6)
        output = "####\n####\n####\n####\n####\n####\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_19rectangle(self):
        """ 19th test case """
        r1 = Rectangle(2, 2)
        output = "##\n##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_20rectangle(self):
        """ 20th test case """
        r1 = Rectangle(4, 6, 2, 1, 12)
        output = "[Rectangle] (12) 2/1 - 4/6\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)

    def test_21rectangle(self):
        """ 21th test case """
        r1 = Rectangle(2, 3, 2, 2)
        output = "\n\n  ##\n  ##\n  ##\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_22rectangle(self):
        """ 22th test case """
        r1 = Rectangle(3, 2, 1, 0)
        output = " ###\n ###\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1.display()
            self.assertEqual(fake_output.getvalue(), output)

    def test_23rectangle(self):
        """ 23th test case """
        r1 = Rectangle(10, 10, 10, 10, 65)
        output = "[Rectangle] (65) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(89)
        output = "[Rectangle] (89) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(89, 2)
        output = "[Rectangle] (89) 10/10 - 2/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(89, 2, 3)
        output = "[Rectangle] (89) 10/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(89, 2, 3, 4)
        output = "[Rectangle] (89) 4/10 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(89, 2, 3, 4, 5)
        output = "[Rectangle] (89) 4/5 - 2/3\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)

    def test_24rectangle(self):
        """ 24th test case """
        r1 = Rectangle(10, 10, 10, 10, 65)
        output = "[Rectangle] (65) 10/10 - 10/10\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(height=1)
        output = "[Rectangle] (65) 10/10 - 10/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(width=1, x=2)
        output = "[Rectangle] (65) 2/10 - 1/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(y=1, width=2, x=3, id=89)
        output = "[Rectangle] (89) 3/1 - 2/1\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)
        r1.update(x=1, height=2, y=3, width=4)
        output = "[Rectangle] (89) 1/3 - 4/2\n"
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            self.assertEqual(fake_output.getvalue(), output)

    def test_25rectangle(self):
        """ 25th test case """
        r1 = Rectangle(10, 2, 1, 9, 89)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle(1, 1, 0, 0, 75)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            print(type(r1_dictionary))
            print(r2)
            output = "[Rectangle] (89) 1/9 - 10/2\n<class 'dict'>\n[Rectangle] (75) 0/0 - 1/1\n"
            self.assertEqual(fake_output.getvalue(), output)

        r2.update(**r1_dictionary)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r2)
            print(r1 == r2)
            output = "[Rectangle] (89) 1/9 - 10/2\nFalse\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_26rectangle(self):
        """ 26th test case """
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(type(dictionary))
            print(type(json_dictionary))
            output = "<class 'dict'>\n<class 'str'>\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_27rectangle(self):
        """ 27th test case """
        r1 = Rectangle(3, 5, 1, 0, 43)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)
        with patch('sys.stdout', new=StringIO()) as fake_output:
            print(r1)
            print(r2)
            print(r1 is r2)
            print(r1 == r2)
            output = "[Rectangle] (43) 1/0 - 3/5\nRectangle] (43) 1/0 - 3/5\nFalse\nFalse\n"
            self.assertEqual(fake_output.getvalue(), output)

    def test_27rectangle(self):
        """ 28th test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1 = Rectangle(10, 7, 2, 8, 20)
            r2 = Rectangle(2, 4, 0, 0, 21)
            list_rectangles_input = [r1, r2]
            Rectangle.save_to_file(list_rectangles_input)
            list_rectangles_output = Rectangle.load_from_file()
            self.assertNotEqual(list_rectangles_input, list_rectangles_output)
            for rect1, rect2 in zip(list_rectangles_input, list_rectangles_output):
                self.assertNotEqual(id(rect1), id(rect2))

    def test_rectangle27(self):
        """ Correction test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle.save_to_file(None)
            output = Rectangle.load_from_file()
            print(len(output))
            self.assertEqual(fake_output.getvalue(),"0\n")

    def test_rectangle28(self):
        """ Correction test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle.save_to_file([])
            output = Rectangle.load_from_file()
            print(len(output))
            self.assertEqual(fake_output.getvalue(),"0\n")

    def test_rectangle29(self):
        """ Correction test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            Rectangle.save_to_file([Rectangle(1, 2)])
            output = Rectangle.load_from_file()
            obj = output[0]
            print(obj)
            self.assertEqual(fake_output.getvalue(), '[Rectangle] (28) 0/0 - 1/2\n')

    def test_rectangle30(self):
        """ Correction test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            if os.path.exists("Rectangle.json"):
                os.remove("Rectangle.json")
            output = Rectangle.load_from_file()
            print(len(output))
            self.assertEqual(fake_output.getvalue(),"0\n")


    def test_28rectangle(self):
        """ 29th test case """
        with patch('sys.stdout', new=StringIO()) as fake_output:
            r1 = Rectangle(10, 7, 2, 8, 20)
            r2 = Rectangle(2, 4, 0, 0, 21)
            list_rectangles_input = [r1, r2]
            Rectangle.save_to_file_csv(list_rectangles_input)
            list_rectangles_output = Rectangle.load_from_file_csv()
            self.assertNotEqual(list_rectangles_input, list_rectangles_output)
            for rect1, rect2 in zip(list_rectangles_input, list_rectangles_output):
                self.assertNotEqual(id(rect1), id(rect2))


    def suite(self):
        suite = unittest.TestSuite()
        suite.addTest(self.test_2rectangle())
        suite.addTest(self.test_3rectangle())
        suite.addTest(self.test_4-rectangle())
        suite.addTest(self.test_5-rectangle())
        suite.addTest(self.test_6-rectangle())
        suite.addTest(self.test_7-rectangle())
        suite.addTest(self.test_8-rectangle())
        suite.addTest(self.test_10-rectangle())
        suite.addTest(self.test_11-rectangle())
        suite.addTest(self.test_12-rectangle())
        suite.addTest(self.test_13-rectangle())
        suite.addTest(self.test_14-rectangle())
        suite.addTest(self.test_15-rectangle())
        suite.addTest(self.test_16-rectangle())
        suite.addTest(self.test_17-rectangle())
        suite.addTest(self.test_18-rectangle())
        suite.addTest(self.test_19-rectangle())
        suite.addTest(self.test_20-rectangle())
        return suite

    if __name__ == '__main__':
        runner = unittest.TextTestRunner()
        runner.run(MyTestClass().suite())
