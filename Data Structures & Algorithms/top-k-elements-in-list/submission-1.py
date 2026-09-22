class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {num : 0 for num in nums}
        for num in nums:
            freq[num] += 1
        
        buckets = [[] for i in range(len(nums) + 1)]
        for key in freq:
            buckets[freq[key]].append(key)

        res = []
        for i in range(len(nums), -1, -1):
            if len(res) == k:
                break

            for num in buckets[i]:
                res.append(num)

        return res
