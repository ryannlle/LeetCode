class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hash_table = {}

        for num in nums:
            hash_table[num] = hash_table.get(num, 0) + 1

        max_count = 0
        majority = 0

        for num, count in hash_table.items():
            if count > max_count:
                max_count = count
                majority = num

        return majority