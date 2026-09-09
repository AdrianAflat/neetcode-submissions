class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq = {i : [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visit = set()
        cycle = set()
        def dfs(course):
            if course in cycle: 
                return False
            if course in visit:
                return True

            cycle.add(course)
            for pre in prereq[course]:
                if dfs(pre) == False:
                    return False

            cycle.remove(course)
            visit.add(course)
            output.append(course)
            return True

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output