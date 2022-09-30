#!/usr/bin/python3
"""The Square module"""
from models.rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x , y, id)

    @property
    def size(self):
        """size of a rectangle"""
        return self.width

    @size.setter
    def size(self, value):
        """setter size"""
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    def update(self, *args, **kwargs):
        if len(args) > 0:
            lp = ["id", "size", "x", "y"]
            for i, k in zip(lp, args):
                setattr(self, i, k)
        else:
            for i, k in kwargs.items():
                if hasattr(self, i):
                    setattr(self, i, k)

    def to_dictionary(self):
        attributes = ["id", "size", "x", "y"]
        return {key: getattr(self, key) for key in attributes}

