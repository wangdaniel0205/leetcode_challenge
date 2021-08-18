class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        flag = False
        res = 0
        for c in reversed(s):
            if ord(c) >= 65 and ord(c) <= 122:
                res += 1
                flag = True
            elif flag:
                break
                
        return res