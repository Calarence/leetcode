class Solution(object):
    def addZeroToList(self,num,list):
        for index in range(num):
            list.append('0')
        return list

    def getFormatedList(self,version1,version2):
        list1 = version1.split('.')
        list2 = version2.split('.')
        length = len(list1) - len(list2)
        if length <= 0:
            length = -(length)
            list1 = self.addZeroToList(length,list1)
        else:
            list2 = self.addZeroToList(length,list2)
        return list1,list2        
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        list1, list2 = self.getFormatedList(version1,version2)
        print(list1,list2)
        index = 0
        while index < len(list1):
            if int(list1[index]) > int(list2[index]):
                return 1
            elif int(list1[index]) < int(list2[index]):
                return -1
            else:
                index += 1
        return 0

