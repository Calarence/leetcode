class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        下面的优化更加简洁
        """
        s1 = []
        if len(s) == 0:
            return 0
        elif " " in s:
            s1 = s.strip(" ").split(" ")
            return len(s1[-1])
        else:
            return len(s)
class  optimization(object):
    """docstring for  opti"""
    def lengthOfLastWord(self, s):
        list = s.split()
        return len(list[-1]) if list != [] else 0
        