class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        k = 1

        for n in range(1, len(nums)):
            if nums[n] != nums[n - 1]:
                nums[k] = nums[n]
                k += 1
        return k