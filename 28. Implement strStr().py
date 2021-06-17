class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        
        if len(needle) == 0:
            return 0

        for l in range(len(haystack) - (len(needle)-1)):
            if haystack[l] == needle[0]:
                if needle == haystack[l:l+len(needle)]:
                    return l
            
        return -1