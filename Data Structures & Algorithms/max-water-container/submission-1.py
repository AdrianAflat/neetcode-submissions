class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0 # max amount of water

        l = 0
        r = len(heights) - 1
        while l < r:
            water = (r - l) * min(heights[l], heights[r])
            if water > res:
                res = water

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1

        return res
