import unittest

from calc import subtract_func

class TestSubtract(unittest.TestCase):

	def test_subtract_test(self):
		arg_ints = [20, 5, 5, 5]
		sub_result = subtract_func(arg_ints)
		self.assertEqual(sub_result, 5)
	
	def test_non_below_zero(self):
		arg_ints = [20, 10, 10, 10]
		sub_result = subtract_func(arg_ints)
		self.assertEqual(sub_result, 0)

if __name__ == '__main__':
	unittest.main()
