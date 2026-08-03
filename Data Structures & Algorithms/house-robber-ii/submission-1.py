class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp1 = [0] * (n - 1)
        dp2 = [0] * (n - 1)

        if n == 1:
            return nums[0] 
        if n == 2:
            return (max(nums[0], nums[1]))

        def rob(cache, houses):
            cache[0] = houses[0]
            cache[1] = max(houses[0], houses[1])

            for i in range(2, len(houses)):
                cache[i] = max(houses[i] + cache[i - 2], cache[i - 1])

            return cache[len(houses) - 1]

        return max(rob(dp1, nums[0:n - 1]), rob(dp2, nums[1:n]))
       
