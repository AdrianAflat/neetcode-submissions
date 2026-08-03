class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [0] * (len(nums) - k + 1)

        l = 0
        r = k - 1
        while r < len(nums):
            m = max(nums[l:r + 1])
            result[l] = m 

            l += 1
            r += 1

        return result