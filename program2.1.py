import pytest
import unittest

def numwords(string):
    results = len(string.split())
    return results

def pytest():
    #pytest test
    s = input("Give me an input of 1: ")
    assert numwords(s) == 1
    s = input("Give me an input of 2: ")
    assert numwords(s) == 2
    s = input("Give me an input of 3: ")
    assert numwords(s) == 3
    s = input("Give me an input of 4: ")
    assert numwords(s) == 4
    s = input("Give me an input of 5: ")
    assert numwords(s) == 5

print("----------PYTEST----------")
pytest()
print("----------END TEST--------")
 