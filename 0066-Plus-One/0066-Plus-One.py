class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        temp  = ""
        for num in digits:
            temp += str(num)

        temp = int(temp) + 1
        temp = str(temp)
        new = []

        for num in temp:
            new.append(int(num))

        return new
