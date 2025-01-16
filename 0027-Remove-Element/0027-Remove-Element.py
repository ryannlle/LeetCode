class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        m = 0
        for k in range(len(nums)):
            if nums[k] == val:
                nums[k] = 101
                m += 1
        nums.sort()
        return len(nums) - m
