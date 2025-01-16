class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if m == 0:
            for i in range(len(nums2)):
                nums1[i] = nums2[i]
        elif n == 0:
            return
        for x in range(m, m + n):
            nums1[x] = nums2[x - m]
        nums1.sort()

