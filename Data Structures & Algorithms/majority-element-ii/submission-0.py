class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
            
        target = len(nums) // 3
        res = []
        for num in count:
            if count[num] > target:
                res.append(num)

        return res