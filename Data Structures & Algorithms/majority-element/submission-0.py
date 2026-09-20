class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 1
        prev = nums[0] 
        for i in range(1, len(nums)):
            if nums[i] == prev:
                count += 1
            elif nums[i] != prev:
                count -= 1

            if count <= 0:
                prev = nums[i]

        return prev
