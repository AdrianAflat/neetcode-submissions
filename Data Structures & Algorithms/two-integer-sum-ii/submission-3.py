class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [1,2,3,4]  target = 7 (passes)
        # [2, 3, 4]  target = 6
            
        result = [0] * 2 
        l = 0 
        r = 1

        length = len(numbers)
        while l < length: 
            while r < length:
                if numbers[l] + numbers[r] == target:
                    result[0] = l + 1
                    result[1] = r + 1 
                    break 
            
                r += 1

            l += 1
            r = l + 1

        return result