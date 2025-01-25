class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        high = len(nums) - 1
        low = 0

        while (low <= high):
            mid = (high + low) // 2
            if (target == nums[mid]):
                return mid
            if (target > nums[mid]):
                low = mid + 1
            if (target < nums[mid]):
                high = mid - 1


        return low




