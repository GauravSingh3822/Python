import os,sys
from os.path import dirname,join,abspath

sys.path.insert(0, abspath(join(dirname(__file__),'..'))) ##dunder or magic method


def course():
    print("This is my course details")

