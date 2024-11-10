import math

def simplify(frac):
  gcd = math.gcd(frac[0], frac[1]) # zastąpiło fractions.gcd()
  return [frac[0] // gcd, frac[1] // gcd]

def add_frac(frac1, frac2):             # frac1 + frac2
  return simplify([frac1[0] * frac2[1] + frac2[0] * frac1[1], frac1[1] * frac2[1]])

def sub_frac(frac1, frac2):             # frac1 - frac2
  return simplify([frac1[0] * frac2[1] - frac2[0] * frac1[1], frac1[1] * frac2[1]])

def mul_frac(frac1, frac2):             # frac1 * frac2
  return simplify([frac1[0] * frac2[0], frac1[1] * frac2[1]])

def div_frac(frac1, frac2):             # frac1 / frac2
  return simplify([frac1[0] * frac2[1], frac1[1] * frac2[0]])

def is_positive(frac):                  # bool, czy dodatni
  return frac[0] * frac[1] > 0

def is_zero(frac):                     # bool, typu [0, x]
  return frac[0] == 0

def cmp_frac(frac1, frac2):             # -1 | 0 | +1
  if frac1[0] * frac2[1] > frac2[0] * frac1[1]:
    return 1
  elif frac1[0] * frac2[1] < frac2[0] * frac1[1]:
    return -1
  return 0

def frac2float(frac):                   # konwersja do float
  return frac[0] / frac[1]

# f1 = [-1, 2]      # -1/2
# f2 = [1, -2]      # -1/2 (niejednoznaczność)
# f3 = [0, 1]       # zero
# f4 = [0, 2]       # zero (niejednoznaczność)
# f5 = [3, 1]       # 3
# f6 = [6, 2]       # 3 (niejednoznaczność)

import unittest

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
        self.assertEqual(add_frac([-1, 2], [1, 2]), [0, 1])

    def test_sub_frac(self): 
        self.assertEqual(sub_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(sub_frac([-1, 2], [1, 2]), [-1, 1])

    def test_mul_frac(self):
        self.assertEqual(mul_frac([1, 2], [1, 3]), [1, 6])
        self.assertEqual(mul_frac([-1, 2], [1, 2]), [-1, 4])

    def test_div_frac(self):
        self.assertEqual(div_frac([1, 2], [1, 3]), [3, 2])
        self.assertEqual(div_frac([-1, 2], [1, 2]), [-1, 1])

    def test_is_positive(self):
        self.assertTrue(is_positive([1, 2]))
        self.assertFalse(is_positive([-1, 2]))

    def test_is_zero(self):
        self.assertTrue(is_zero([0, 1]))
        self.assertFalse(is_zero([1, 2]))

    def test_cmp_frac(self):
        self.assertEqual(cmp_frac([1, 2], [1, 3]), 1)
        self.assertEqual(cmp_frac([1, 2], [2, 4]), 0)
        self.assertEqual(cmp_frac([1, 2], [3, 4]), -1)

    def test_frac2float(self):
        self.assertEqual(frac2float([1, 2]), 0.5)

    def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy