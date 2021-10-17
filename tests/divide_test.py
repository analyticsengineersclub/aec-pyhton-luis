import unittest

from calc import divide_func

class TestDivide(unittest.TestCase):

	def test_subtract_test(self):
		arg_ints = [20, 5]
		sub_result = divide_func(arg_ints)
		self.assertEqual(sub_result, 4)
	
	def test_non_zero_denom(self):
		arg_ints = [20, 0]
		sub_result = divide_func(arg_ints)
		self.assertEqual(sub_result, 0)

if __name__ == '__main__':
	unittest.main()