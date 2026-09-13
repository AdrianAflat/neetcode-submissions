class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = {i:[] for i in range(numCourses)}
        for c1, c2 in prerequisites:
            adj[c1].append(c2)

        
        def dfs(node, target, visited):
            if node == target:
                return True

            if node in visited:
                return False
            
            visited.add(node)

            for j in adj[node]:
                if dfs(j, target, visited):
                    return True

            return False

        res = []
        for c1, c2 in queries:
            if dfs(c1, c2, set()):
                res.append(True)
            else:
                res.append(False)

        return res