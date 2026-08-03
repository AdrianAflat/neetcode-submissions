class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # number : frequency of that number
        for num in nums:
            count[num] = count.get(num, 0) + 1

        bucket = [[] for i in range(len(nums) + 1)]  

        for num, freq in count.items():
            bucket[freq].append(num)

        res = []
        for i in range(len(nums), 0, -1):
            res.extend(bucket[i])
            if len(res) >= k:
                break

        return res
            