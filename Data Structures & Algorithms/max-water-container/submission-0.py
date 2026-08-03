class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # [1,7,2,5,4,7,3,6]
        #  6 * min(6, 7)

        l = 0
        r = len(heights) - 1

        result = 0 
        while l < r:
            water = min(heights[l], heights[r]) * (r - l) 
            if water > result:
                result = water 

            if heights[l] > heights[r]:
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1

        return result