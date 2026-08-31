class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digitToChar = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        res = []
        def dfs(i, sublist):
            if len(sublist) == len(digits):
                res.append(sublist)
                return 

            for c in digitToChar[digits[i]]:
                dfs(i + 1, sublist + c)

        if not digits:
            return []

        dfs(0, "")
        return res
        
