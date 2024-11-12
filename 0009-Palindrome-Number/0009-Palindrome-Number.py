class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        else:
            x = str(x)
            y = x[::-1]

            for i in range(len(x) / 2):
                if x[i] != y[i]:
                    return False

            return True