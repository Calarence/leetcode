import unittest
from main import Optimize
class TestOptimize(unittest.TestCase):
	"""docstring for TestOptimize"""
	def setUp(self):
		self.optimize = Optimize()

	def test_twoNum(self):
		print(self.optimize.twoSum([1,2,3],6))

if __name__ == '__main__':
	unittest.main()


