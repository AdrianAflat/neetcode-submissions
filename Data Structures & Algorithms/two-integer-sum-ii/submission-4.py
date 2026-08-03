class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [1,2,3,4]  target = 7 (passes)
        # [2, 3, 4]  target = 6
            
        result = [0] * 2 
        l = 0 
        r = len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                result[0] = l + 1
                result[1] = r + 1
                break 
            elif numbers[l] + numbers[r] < target:
                l += 1
            elif  numbers[l] + numbers[r] > target:
                r -= 1

        return result
        