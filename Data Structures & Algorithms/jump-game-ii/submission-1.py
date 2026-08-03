class Solution:
    def jump(self, nums: List[int]) -> int:
        # start at index 0
        # iterate through the indexes that can be jumped to 
        # check if you can reach the end else:
        #   take the max index and move to that 

        # [2,4,1,1,1,1]
        #  l
        #      r

        result = 0
        l = 0
        r = 0
        while r < len(nums) - 1:
            farthest = 0
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            l = r + 1
            r = farthest 
            result += 1

        return result

        