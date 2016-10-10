import unittest
from stack import Stack
from main import Solution
class TestStack(unittest.TestCase):
	"""docstring for TestMain"""
	def setUp(self):
		self.stack = Stack()
		self.stack.push(1)
		self.stack.push(2)
		self.stack.push(3)
	def test_insert(self):
		self.assertFalse(self.stack.isEmpty())

	def test_pop(self):
		self.assertEqual(self.stack.pop(),3)
	def test_top(self):
		self.assertEqual(self.stack.top(),3)

class TestMain(unittest.TestCase):
	"""docstring for TestMain"""
	def setUp(self):
		self.solution = Solution()
	@unittest.skip("this is useless")
	def test_collector(self):
		print(self.solution.collector("adfadf"))

	# def test_getMiddle(self):
	# 	self.assertEqual(self.solution.getMiddle("aaa"),1)

	def test_getMiddle(self):
		self.assertEqual(self.solution.getMiddle([1,2,3,4]),2)

	def test_isPalindrome(self):
		self.assertTrue(self.solution.isPalindrome(""))
		self.assertTrue(self.solution.isPalindrome("a"))
		self.assertTrue(self.solution.isPalindrome("aba"))
		# self.assertTrue(self.solution.isPalindrome("ancd"))
		self.assertTrue(self.solution.isPalindrome("0P"))
	
	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main()