class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        subset = []
        def backtrack(i):
            if subset not in res:
                res.append(subset.copy())

            if i >= len(nums):
                return

            subset.append(nums[i])
            backtrack(i + 1)

            subset.pop()
            backtrack(i + 1)


        backtrack(0)
        return res