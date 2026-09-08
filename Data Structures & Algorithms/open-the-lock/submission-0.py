class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # 0 0 0 0
        # 1 1 1 1
        # 2 2 2 2
        # 3 3 3 3 
        # 4 4 4 4
        # 5 5 5 5
        # 6 6 6 6
        # 7 7 7 7
        # 8 8 8 8
        # 9 9 9 9

        if "0000" in deadends:
            return -1 

        def children(lock):
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])

                digit = str((int(lock[i]) - 1 + 10) % 10)
                res.append(lock[:i] + digit + lock[i + 1:])
            
            return res


        q = deque()
        q.append(["0000", 0]) # lock, turns
        visit = set(deadends) 
        while q:
            lock, turns = q.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    q.append([child, turns + 1])

        return -1
            