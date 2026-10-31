class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res = float('inf')
        curSum = 0
        l = 0
        r = 0
        while r < len(nums):
            curSum += nums[r]
            
            while curSum >= target:
                res = min(res, (r - l + 1))
                curSum -= nums[l]
                l += 1

            r += 1

        if res == float('inf'):
            return 0
        else:
            return int(res)
            
        # 2 1 5 1 5 3   target = 10
        #     l
        #           r

        #curSum = 9
        #res = 5