class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        t1, t2, t3 = target
        for triple in triplets:
            if triple[0] > t1 or triple[1] > t2 or triple[2] > t3:
                triplets.remove(triple)

        v1 = False
        v2 = False
        v3 = False
        for triple in triplets:
            if t1 == triple[0]:
                v1 = True
            
            if t2 == triple[1]:
                v2 = True

            if t3 == triple[2]:
                v3 = True

        if v1 and v2 and v3:
            return True
        else:
            return False 