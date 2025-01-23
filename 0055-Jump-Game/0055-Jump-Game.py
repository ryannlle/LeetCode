class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        end = len(nums) - 1
        max_reach = 0
        steps = 0
        while steps <= max_reach:
            max_reach = max(max_reach, steps + nums[steps])

            if max_reach >= end:
                return True

            steps += 1
        return False