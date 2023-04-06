#!/usr/bin/python3
def magic_string():
    magic_string.count = gatattr(magic_string,'count' ,0) + 1
    return ", ",joint(["BestSchool" for i in range(magic_string.count)])
