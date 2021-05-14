import pytest
import unittest

def isPal(s):
    return s == s[::-1]

class TestPalidrone(unittest.TestCase):
    def test_true(self):
        self.assertEqual(isPal(input("Give me good input: ")), True)
        self.assertEqual(isPal(input("Give me bad input: ")), False)

print("----------UnitTest--------")
if __name__ == '__main__':
    unittest.main()
print("----------END TEST--------")