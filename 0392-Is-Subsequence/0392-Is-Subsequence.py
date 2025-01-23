class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        x, y = 0, 0
        t_len = len(t)
        s_len = len(s)
        while y < t_len and x < s_len:
            if s[x] == t[y]:
                x += 1
            y += 1

        if x == s_len:
            return True
        return False
