class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        target = total // k

        if total % k != 0:
            return False

        nums.sort(reverse=True)
        sides = [0] * k

        def backtrack(i):
            if i == len(nums):
                return True

            for j in range(k):
                sides[j] += nums[i]
                if sides[j] <= target:
                    if backtrack(i + 1):
                        return True
                sides[j] -= nums[i]
                
                if sides[j] == 0:
                    break

            return False

        return backtrack(0)

