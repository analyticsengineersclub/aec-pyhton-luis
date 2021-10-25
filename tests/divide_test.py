import unittest

from calc import divide_func

class TestDivide(unittest.TestCase):

	def test_divide_test(self):
		ints_to_divide = [20, 5]
		our_division = divide_func(ints_to_divide)
		self.assertEqual(our_division, 4)
	
	def test_non_zero_denom(self):
		ints_to_divide = [20, 0]
		our_division = divide_func(ints_to_divide)
		self.assertEqual(our_division, 0)
	
	def test_n_args(self):
		with self.assertRaises(Exception):
			divide_func([1, 2, 3])

if __name__ == '__main__':
	unittest.main()