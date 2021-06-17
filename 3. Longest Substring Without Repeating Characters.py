class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = maxLen = 0
        hashDict = {}
        
        for i, c in enumerate(s):
            if c in hashDict.keys() and start <= hashDict[c]:
                start = hashDict[c]+1
            else:
                maxLen = max(maxLen, i-start+1)
            
            hashDict[c] = i
        return maxLen
