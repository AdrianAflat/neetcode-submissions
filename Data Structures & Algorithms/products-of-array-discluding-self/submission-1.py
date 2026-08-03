class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # [1,2,4,6]
        # [48,24,12,8]

        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        
        # calculate prefix
        prod = 1
        for i in range(len(nums)):
            prefix[i] = nums[i] * prod 
            prod = prefix[i]

        # calculate postfix
        prod = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = nums[i] * prod 
            prod = postfix[i]

        res = [0] * len(nums)
        for i in range(len(nums)):
            if 0 <= i - 1 <= len(nums):
                pre = prefix[i - 1]
            else:
                pre = 1

            if 0 <= i + 1 <= len(nums) - 1:
                post = postfix[i + 1]
            else:
                post = 1

            val = pre * post
            res[i] = val

        return res