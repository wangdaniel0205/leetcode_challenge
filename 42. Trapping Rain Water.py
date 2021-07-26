class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if len(height) <= 2:
            return 0 
        
        left, right, res = 0, len(height)-1, 0

    
    
    
        while left < right:
            if height[left] <= height[right]:
                k = left + 1
                while height[k] < height[left]:
                    res += height[left] - height[k]
                    k += 1
                left = k
            else:
                k = right - 1
                while height[k] < height[right]:
                    res += height[right] - height[k]
                    k -= 1
                right = k
    
        return res
    
        
        