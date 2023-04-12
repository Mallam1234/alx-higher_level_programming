#!/usr/bin/ python3
def lookup(obj):
    """function that returns the list of available attributes 
        and methods of an object

    Agrs: 
        obj: instance of the class 

        Returns:
            List of attributes
        """

        return dir(obj)
