import unittest

def add(x,y):
    return x+y

class TestSum(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(add(4,5),8,"sum value is 9")

    def test_sum_neg(self):
        self.assertEqual(add(4,-5),-1,"sum value is -1")

if __name__== '__main__':
    unittest.main()

# .assertEqual(a, b)	a == b
# .assertTrue(x)	bool(x) is True
# .assertFalse(x)	bool(x) is False
# .assertIs(a, b)	a is b
# .assertIsNone(x)	x is None
# .assertIn(a, b)	a in b
# .assertIsInstance(a, b)	isinstance(a, b)