class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        
        table = {}
        
        for s in strs:
            
            #insertion sort
            l = []
            for c in s:
                i = 0
                for k in l:
                    if k >= c:
                        break
                    i += 1
                l.insert(i,c)
        
            # to hash table
            h = hash(tuple(l))
            if h in table:
                table[h].append(s)
            else:
                table[h] = [s]
        
        return list(table.values())