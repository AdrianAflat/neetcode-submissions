class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        m = {}
        res = [0, 0]
        for i, n in enumerate(nums):
            if (target - n) in m:
                res[0] = m[(target - n)]
                res[1] = i
            else:
                m[n] = i

        return res
