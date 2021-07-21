class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        
        1. make hash table
        2. fill the hash table if number is positive O(n)
        3. search from 1 to hash table until one does not exists, smaller than O(n)
        
        
        
        
        def exists(intTable, val):
            if val % 2 == 1: # if val is odd
                digit = val//2
                return (intTable // 10**digit % 10) % 2 == 1
            else:
                digit = (val//2)-1
                return 10**digit < intTable and intTable // 10**digit % 10 >= 2
        
        def add(intTable, val):
            if val % 2 == 1: # if val is odd
                digit = val//2
                intTable += 10**digit
            else:
                digit = (val//2)-1
                intTable += 10**digit * 2
            return intTable 
        
        intTable = 0
        for val in nums:
            if val <= 0 or exists(intTable, val):
                continue
            intTable = add(intTable, val)
            
        i = 0
        for c in str(intTable)[::-1]:
            if c != '3':
                return i*2+2 if c == '1' else i*2+1
            i+=1
        return i*2+2 if c == '1' else i*2+1
        """  

        num_len = len(nums)
        nums.append(-1)
        for i in range(num_len):
            while not(nums[i] < 1 or nums[i] > num_len or nums[nums[i]] == nums[i]):
                temp = nums[i]
                nums[i] = nums[nums[i]]
                nums[temp] = temp

        for i in range(1, num_len+1):
            if nums[i] != i:
                return i
        return num_len+1