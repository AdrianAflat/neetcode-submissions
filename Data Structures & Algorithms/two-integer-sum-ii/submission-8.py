class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        res = [-1, -1]
        
        while l <= r:
            curSum = numbers[l] + numbers[r]
            if curSum == target:
                res[0] = l + 1
                res[1] = r + 1
                break
            
            if curSum > target:
                r -= 1
            else:
                l += 1

        return res
            
            
