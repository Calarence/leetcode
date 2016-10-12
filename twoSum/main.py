class Solution(object):
    """
    时间复杂度 O(n^2)
    空间复杂度 O(1)

    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for index in range(0,len(nums)):
            for next in range(index+1,len(nums)):
                if nums[index] + nums[next] == target:
                    return [index,next]
                else: continue
                

class Optimize(object):
    """
    时间复杂度 O(n)
    空间复杂度 O(n)
    """
    def twoSum(self,nums,target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        map = {}
        for index in range(len(nums)):
            wanted = target - nums[index]
            if wanted in map:
                return [map.get(wanted),index]
            map[nums[index]] = index
        raise ValueError("No two sum solution")


    
        

        