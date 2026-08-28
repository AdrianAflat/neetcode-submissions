class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        sublist = []
        chosen = [False] * len(nums)
        def backtrack():
            if len(sublist) >= len(nums):
                res.append(sublist.copy())
                return

            for i in range(len(nums)):
                if chosen[i] == False:
                    sublist.append(nums[i])
                    chosen[i] = True
                    backtrack()

                    sublist.pop()
                    chosen[i] = False
                    backtrack

        backtrack()
        return res