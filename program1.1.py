import pytest
import unittest

def isPal(s):
    return s == s[::-1]

def pytest():
    #pytest test
    s = input("Give me good input: ")
    assert isPal(s) == True
    s = input("Give me bad input: ")
    assert isPal(s) == False

print("----------PYTEST----------")
pytest()
print("----------END TEST--------")
 