import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "devilparser",
    version = "0.0.2",
    author = "Drew Stinnett",
    author_email = "drew@drewlink.com",
    description = ("Load RC type files with the ability to use shell commands like lpass to get passwords"),
    license = "BSD",
    keywords = "lpass secuirty config",
    packages=['devilparser',],
    scripts=['scripts/devilparser-cat.py'],
    long_description=read('README.md'),
)
