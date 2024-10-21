#!/usr/bin/python3
""" Defines class 'square' """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class square """
    def __init__(self, size, x=0, y=0, id=None):
        """ class 'Square' constructor """
        super().validator("width", size, 0)
        super().validator("x", 1, x)
        super().validator("y", 1, y)
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns a string representation of a square """
        return "[Square] ({:d}) {:d}/{:d} - {:d}\
".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ returns the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ sets value for size """
        Rectangle.validator("width", value, 0)
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ Updates class 'Square' """
        if args:
            for i in range(len(args)):
                if i == 0:
                    if type(args[i]) == int:
                        self.id = args[i]
                elif i == 1:
                    Rectangle.validator("width", args[i], 0)
                    self.width = args[i]
                    self.height = args[i]
                elif i == 2:
                    Rectangle.validator("x", 1, args[i])
                    self.x = args[i]
                elif i == 3:
                    Rectangle.validator("y", 1, args[i])
                    self.y = args[i]
        else:
            if 'id' in kwargs:
                if type(kwargs['id']) == int:
                    self.id = kwargs['id']
            if 'size' in kwargs:
                Rectangle.validator("width", kwargs['size'], 0)
                self.width = kwargs['size']
                self.height = kwargs['size']
            if 'x' in kwargs:
                Rectangle.validator("x", 1, kwargs['x'])
                self.x = kwargs['x']
            if 'y' in kwargs:
                Rectangle.validator("y", 1, kwargs['y'])
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary of class Rectangle attributes """
        return {'size': self.width, 'x': self.x, 'y': self.y, 'id': self.id}
