#!/usr/bin/python3
""" Defines class 'Rectangle' """
from models.base import Base
" # Base = __import__('base').Base"


class Rectangle(Base):
    """ The class 'Rectangle' """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ class 'Rectangle constructor """
        super().__init__(id)
        Rectangle.validator("width", width, 0)
        Rectangle.validator("height", height, 0)
        Rectangle.validator("x", 1, x)
        Rectangle.validator("y", 1, y)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ width getter function """
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter function """
        Rectangle.validator("width", value, 0)
        self.__width = value

    @property
    def height(self):
        """ height getter function """
        return self.__height

    @height.setter
    def height(self, value):
        """ height setter function """
        Rectangle.validator("height", value, 0)
        self.__height = value

    @property
    def x(self):
        """ x getter function """
        return self.__x

    @x.setter
    def x(self, value):
        """ x setter function """
        Rectangle.validator("x", 1, value)
        self.__x = value

    @property
    def y(self):
        """ y getter function """
        return self.__y

    @y.setter
    def y(self, value):
        """ y setter function """
        Rectangle.validator("y", 1, value)
        self.__y = value

    @staticmethod
    def validator(name, value, value2):
        """ validates data before it is assigned to a variable """
        if type(value) != int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{:s} must be > 0'.format(name))
        if type(value2) != int:
            raise TypeError('{:s} must be an integer'.format(name))
        if value2 < 0:
            raise ValueError('{:s} must be >= 0'.format(name))

    def area(self):
        """ returns area of a rectangle """
        return self.__width * self.__height

    def display(self):
        """ Prints a rectangle using character '#' """
        for i in range(self.__y):
            print("")
        for i in range(self.__height):
            for k in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print('#', end='')
            print("")

    def __str__(self):
        """ returns a string of rectangle details """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}\
".format(self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """ Updates class 'Rectangle' """
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) == int:
                        self.id = args[i]
                elif i == 1:
                    Rectangle.validator("width", args[i], 0)
                    self.__width = args[i]
                elif i == 2:
                    Rectangle.validator("height", args[i], 0)
                    self.__height = args[i]
                elif i == 3:
                    Rectangle.validator("x", 1, args[i])
                    self.__x = args[i]
                elif i == 4:
                    Rectangle.validator("y", 1, args[i])
                    self.__y = args[i]
        else:
            if 'id' in kwargs:
                if type(kwargs['id']) == int:
                    self.id = kwargs['id']
            if 'width' in kwargs:
                Rectangle.validator("width", kwargs['width'], 0)
                self.__width = kwargs['width']
            if 'x' in kwargs:
                Rectangle.validator("x", 1, kwargs['x'])
                self.__x = kwargs['x']
            if 'height' in kwargs:
                Rectangle.validator("height", kwargs['height'], 0)
                self.__height = kwargs['height']
            if 'y' in kwargs:
                Rectangle.validator("y", 1, kwargs['y'])
                self.__y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary of class Rectangle attributes """
        return (
                {'width': self.width,
                 'height': self.height,
                 'x': self.x, 'y': self.y,
                 'id': self.id}
                )

