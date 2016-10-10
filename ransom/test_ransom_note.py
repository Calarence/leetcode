import unittest
from ransomNote import Solution
class TestRansom(unittest.TestCase):
	"""docstring for TestRansom"""
	def setUp(self):
		self.s = Solution()
		
	def test_letter_frequency(self):
		frequencies = self.s.letter_frequency("dfda")
		self.assertEqual(frequencies['len'],0)
		self.assertEqual(frequencies['d'],2)

	def test_canConstruct(self):
		result=self.s.canConstruct("aac","aa")
		self.assertEqual(False,result)
if __name__ == '__main__':
	unittest.main()