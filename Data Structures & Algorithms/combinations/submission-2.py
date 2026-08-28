class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        sublist = []
        def dfs(i):
            if len(sublist) == k and sublist not in res:
                res.append(sublist.copy())
                return 

            if i > n:
                return

            sublist.append(i)
            dfs(i + 1)

            sublist.pop()
            dfs(i + 1)


        for num in range(1, n + 1):
            dfs(num)

        return res