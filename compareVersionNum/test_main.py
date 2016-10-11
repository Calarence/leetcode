import unittest
from main import Solution
class TestMain(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()
    
    def test_addZeroToList(self):
        list=self.solution.addZeroToList(2,[1,3])
        self.assertEqual(list[3],'0')
    
    def test_compareVersion(self):
        self.assertEqual(self.solution.compareVersion('1.1','1.01.0'),0)
        self.assertEqual(self.solution.compareVersion('0.0.1','0.0.1'),0)
        self.assertEqual(self.solution.compareVersion('1.1.2','1.1'),1)
        self.assertEqual(self.solution.compareVersion('1.2','1.3'),-1)
if __name__ == '__main__':
    unittest.main()
