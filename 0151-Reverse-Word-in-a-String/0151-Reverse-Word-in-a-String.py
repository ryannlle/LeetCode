class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.strip().split()
        words.reverse()
        result = ""
        for i in range(len(words)):
            result += words[i]
            if (i < len(words) - 1):
                result += " "
        return result