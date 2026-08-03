class Solution:
    def findMin(self, nums: List[int]) -> int:
        # [1,2,3,4,5,6]
        # [3,4,5,6,1,2]  4 rotations  length 6
        # index + 1 mod size
        # []

        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m 

        return nums[l]

        # [3,4,5,6,1,2]
        #  L         R 
        #  L     M   r
        #        L   R 
        #  L    R