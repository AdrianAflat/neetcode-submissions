class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(openCnt, closeCnt, sublist):
            if len(sublist) == (2 * n) and openCnt == closeCnt:
                res.append(sublist)
                return 

            if closeCnt > openCnt or openCnt > n:
                return 

            sublist += "("
            backtrack(openCnt + 1, closeCnt, sublist)

            sublist = sublist[:-1]
            
            sublist += ")"
            backtrack(openCnt, closeCnt + 1, sublist)

            #sublist = sublist[:-1]

        backtrack(0, 0, "")
        return res
