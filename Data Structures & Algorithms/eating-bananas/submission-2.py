class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        # piles = [1,4,3,2], h = 9
        #         [1,2,3,4]  h = 9
        #          1 2 2 1   eating 2  takes:  6 h
        #          1 2 1 1   eating 3  takes:  5 h 
        #          1 4 3 2   eating 1  takes: 10 h

        # time to eat pile: math.ceil(x / k) where x is the pile and k is the rate

        def k_works(k):
            hours = 0
            for p in piles:
                hours += math.ceil(p / k)
            return hours <= h

        maxPile = max(piles)

        l = 1
        r = maxPile # 4
        result = r
        while l <= r:
            m = (l + r) // 2

            if k_works(m):
                result = m
                r = m - 1
            else: 
                l = m + 1
    
        return result
      

