#!/usr/bin/python3
"""

This module is composed by a class that dfines a Rectangle


"""


class Rectangle:
    """ class that defines a rectangle """

    def _int_(self, width=0, height=0):
        """ Method that initializes the instance

        Args:
            width: width of the rectangle
            height: height of the rectangle


            """
            self.width = width
            self.height = height

        @property
        def width(self):
            """ method that returns the value of the width

            Returns:
                width of the rectangle


            """

            return self._width

        @width.setter
        def width(self, value):
            """ method that defines the width

            Args:
                value: width

            Raises:
                TypeError: if width is not an integer
                ValueError: if width is less than zero


            """

            if not isinstance(value,int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self._width = value

        @property
        def height(self):
            """ method that returns the value of the height

            Returns:
                height of the rectangle


            """

            return self._height

        @height.setter
        def height(self, value):
            """ method that defines the height

            Agrs:
                value: height

            Raises:
                TypeError: if height is not an integer
                ValueError: if height is less than zero


            """

            if not isinstance(value, int):
                raise TypeError("height must be an interger")
            if value < 0:
                raise ValueError("height must be >= 0")
            self._height = value
