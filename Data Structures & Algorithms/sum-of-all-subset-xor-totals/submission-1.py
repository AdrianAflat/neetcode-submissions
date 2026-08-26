class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
    
        res = [0]

        subset = []
        def dfs(i):
            if i >= len(nums):
                xorRes =  0
                for num in subset:
                    xorRes ^= num
                res[0] += xorRes
                return
            
            subset.append(nums[i])
            dfs(i + 1)

            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res[0]