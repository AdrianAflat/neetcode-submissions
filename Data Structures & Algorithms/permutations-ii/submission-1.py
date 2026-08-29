class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        sublist = []
        used = [False] * len(nums)
        def backtrack(i):
            if i == len(nums) and sublist not in res:
                res.append(sublist.copy())
                return 

            for n in range(len(nums)):
                if used[n] == False:
                    sublist.append(nums[n])
                    used[n] = True
                    backtrack(i + 1)

                    used[n] = False 
                    sublist.pop()

        backtrack(0)
        return res
            