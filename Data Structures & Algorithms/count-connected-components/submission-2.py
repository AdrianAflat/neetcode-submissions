class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {i:[] for i in range(n)}
        for a, b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        seen = set()
        def dfs(node, par):
            if node == par or node in seen:
                return 

            seen.add(node)

            for j in adjList[node]:
                if j != par:
                    dfs(j, node)

        res = 0
        for i in range(n):
            if i not in seen:
                dfs(i, -1)
                res += 1

        return res
        