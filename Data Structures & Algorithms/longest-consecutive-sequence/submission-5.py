class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # [2,20,4,10,3,4,5]
        if not nums: 
            return 0

        s = set(nums)

        starters = []
        for num in s:
            if num - 1 not in s:
                starters.append(num)

        curr_count = 1
        max_count = 1
        for num in starters:

            i = 1
            while num + i in s:
                curr_count += 1
                if curr_count > max_count:
                    max_count = curr_count
                i += 1

            i = 1
            curr_count = 1

        return max_count