#!/usr/bin/python3
"""Module for Rectangle unit test"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.rectangle import __doc__ as doc_check
from models.square import Square
import json
import io

from contextlib import redirect_stdout

class TestRectangleMethods(unittest.TestCase):
    """Class to test the Rectangle Class"""

    def setUp(self):
        """Initialize nb_objects before each test"""
        Base._Base__nb_objects = 0

    def tearDown(self):
        """Cleans up tasks"""
        pass

    def test_docstrings(self):
        self.assertIsNotNone(doc_check)
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIs(hasattr(Rectangle, "__init__"), True)
        self.assertIsNotNone(Rectangle.__init__.__doc__)
        self.assertIs(hasattr(Rectangle, "width"), True)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIs(hasattr(Rectangle, "height"), True)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIs(hasattr(Rectangle, "x"), True)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIs(hasattr(Rectangle, "y"), True)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIs(hasattr(Rectangle, "area"), True)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIs(hasattr(Rectangle, "display"), True)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIs(hasattr(Rectangle, "__str__"), True)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIs(hasattr(Rectangle, "update"), True)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIs(hasattr(Rectangle, "to_dictionary"), True)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)
    
    # ---------------Tests: task 2 and 3--------------------------------
    def test_class(self):
        """Test Rectangle class"""
        self.assertEqual(str(Rectangle), "<class 'models.rectangle.\
Rectangle'>")

    def test_inheritance(self):
        """Test if Rectangle inherits from Base"""
        self.assertTrue(issubclass(Rectangle, Base))

    def test_init_no_args(self):
        """Test Rectangle() instantiation without self"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle()
        message = "__init__() missing 2 required positional \
arguments: 'width' and 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_one_arg(self):
        """Test Rectangle() instantiation with a missing argument"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(67)
        message = "__init__() missing 1 required positional argument: 'height'"
        self.assertEqual(str(excep.exception), message)

    def test_init_excedent_args(self):
        """Test Rectangle() instantiation with leftover arguments"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(45, 56, 89, 102, 56, 23)
        message = "__init__() takes from 3 to 6 positional \
arguments but 7 were given"
        self.assertEqual(str(excep.exception), message)

    def test_instantiation(self):
        """Test Rectangle() instantiation with 2 arguments"""
        Rect_test = Rectangle(6, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 8,
               '_Rectangle__width': 6,
               '_Rectangle__x': 0,
               '_Rectangle__y': 0,
               'id': 1}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_instantiation_positional(self):
        """Test Rectangle() positional instantiation"""
        Rect_test = Rectangle(9, 4, 12, 7, 8)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 4,
               '_Rectangle__width': 9,
               '_Rectangle__x': 12,
               '_Rectangle__y': 7,
               'id': 8}
        self.assertEqual(Rect_test.__dict__, dic)

        Rect_test = Rectangle(5, 7, 19, 2)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 7,
               '_Rectangle__width': 5,
               '_Rectangle__x': 19,
               '_Rectangle__y': 2,
               'id': 1}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_instantiation_no_positional(self):
        """Test Rectangle() no positional instantiation"""
        Rect_tst = Rectangle(id=9, x=4, width=12, y=7, height=8)
        self.assertEqual(str(type(Rect_tst)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_tst, Base))
        dic = {'_Rectangle__height': 8,
               '_Rectangle__width': 12,
               '_Rectangle__x': 4,
               '_Rectangle__y': 7,
               'id': 9}
        self.assertEqual(Rect_tst.__dict__, dic)

    def test_mix_positional(self):
        """Test Rectangle() positional/ no positional instantiation"""
        Rect_test = Rectangle(9, 100, 3, id=12, y=7)
        self.assertEqual(str(type(Rect_test)), "<class 'models.\
rectangle.Rectangle'>")
        self.assertTrue(isinstance(Rect_test, Base))
        dic = {'_Rectangle__height': 100,
               '_Rectangle__width': 9,
               '_Rectangle__x': 3,
               '_Rectangle__y': 7,
               'id': 12}
        self.assertEqual(Rect_test.__dict__, dic)

    def test_inheritance_id(self):
        """Test if id is inherits from base"""
        Base._Base__nb_objects = 78
        Rect_test = Rectangle(2, 4)
        self.assertEqual(Rect_test.id, 79)

    def test_getter_setter(self):
        """Test getters and setters"""
        Rect_test = Rectangle(5, 8)
        Rect_test.width = 54
        Rect_test.height = 43
        Rect_test.x = 3
        Rect_test.y = 2
        d = {'_Rectangle__height': 43,
             '_Rectangle__width': 54,
             '_Rectangle__x': 3,
             '_Rectangle__y': 2,
             'id': 1}
        self.assertEqual(Rect_test.__dict__, d)
        self.assertEqual(Rect_test.width, 54)
        self.assertEqual(Rect_test.height, 43)
        self.assertEqual(Rect_test.x, 3)
        self.assertEqual(Rect_test.y, 2)

    def test_arguments_invalid_type(self):
        """Test invalid arguments types"""
        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle("34", 2)
        message = "width must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, "w")
        message = "height must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, 6, "holby")
        message = "x must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(TypeError) as excep:
            Rect_test = Rectangle(89, 6, 7, "betty")
        message = "y must be an integer"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(0, 6)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(-7, 6)
        message = "width must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(9, 0)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(9, -12)
        message = "height must be > 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(89, 6, -5)
        message = "x must be >= 0"
        self.assertEqual(str(excep.exception), message)

        with self.assertRaises(ValueError) as excep:
            Rect_test = Rectangle(89, 6, 6, -8)
        message = "y must be >= 0"
        self.assertEqual(str(excep.exception), message)

        def invalid_types(self):
            """Returns lists with different invalid cases"""
            types = (3.56, float('inf'), float('Nan'), True,
                     (5, ), -6.792, [8], None, {8, 7})
            return types

        def validate_types(self):
            """Test invalid arguments types with different cases"""
            Rect_test = Rectangle(8, 5)
            attributes = ["x", "y", "width", "height"]
            for attr in attributes:
                message = "{} must be an integer".format(attr)
                for invalid in self.invalid_types():
                    with self.assertRaises(TypeError) as excep:
                        setattr(Rect_test, attr, invalid_types)
                    self.assertEqual(str(excep.exception), message)


if __name__ == "__main__":
    unittest.main()