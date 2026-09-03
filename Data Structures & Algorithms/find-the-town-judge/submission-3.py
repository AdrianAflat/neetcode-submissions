class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustToPerson = defaultdict(list) # ai : bi
        personToTrust = defaultdict(list) # bi : ai
        for ai, bi in trust:
            trustToPerson[ai].append(bi)
            personToTrust[bi].append(ai)

        for i in range(1, n + 1):
            if len(personToTrust[i]) == n - 1 and not trustToPerson[i]:
                return i

        return -1
      
        