class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        myList = []
        for x in range(len(nums)):
            for i in range(len(nums)):
                if ((nums[x] + nums[i]) == target and x != i):
                    myList.append(x)
                    myList.append(i)
                    return myList