class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s:
            return []
        
        word_len, total_len = len(words[0]), len(words[0]) * len(words)
        res, hashDict = [], {}
        
        for word in words:
            if word in hashDict.keys():
                hashDict[word] += 1
            else:
                hashDict[word] = 1
        
        i = 0
        while i+total_len <= len(s):
            hash_copy = dict(hashDict)
            for j in range(len(words)):
                word = s[i+j*word_len:i+(j+1)*word_len]
                if not word in words:
                    break
                hash_copy[word] -= 1
            if all(val == 0 for val in hash_copy.values()):
                res.append(i)
                
            i+=1
        
        
        return res