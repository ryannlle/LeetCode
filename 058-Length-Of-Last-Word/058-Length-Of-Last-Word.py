class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s[::-1].strip()
        count = 0
        for i in range(len(s)):
            if s[i] == " ":
                break
            count += 1
        return count
