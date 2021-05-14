import pytest
import unittest

def numwords(string):
    results = len(string.split())
    return results

class TestPalidrone(unittest.TestCase):
    def test_length(self):
        self.assertEqual(numwords(input("Give me an input with 1 word: ")), 1)
        self.assertEqual(numwords(input("Give me an input with 2 word: ")), 2)
        self.assertEqual(numwords(input("Give me an input with 3 word: ")), 3)
        self.assertEqual(numwords(input("Give me an input with 4 word: ")), 4)
        self.assertEqual(numwords(input("Give me an input with 5 word: ")), 5)


print("----------UnitTest--------")
if __name__ == '__main__':
    unittest.main()
print("----------END TEST--------")