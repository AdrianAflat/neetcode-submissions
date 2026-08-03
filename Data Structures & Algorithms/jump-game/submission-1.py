class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        for i in range(len(nums) - 1, -1, -1):
            if i + nums[i] >= goal:
                goal = i

        return True if goal == 0 else False

        # [1,2,0,1,0]
        # if 3 + 1 >= 0