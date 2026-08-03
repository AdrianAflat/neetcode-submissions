#from _typeshed import StrOrLiteralStr
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        seen = set()

        longest = 0

        for r in range(len(s)):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1

            window = (r - l) + 1
            longest = max(longest, window)
            seen.add(s[r])
            r += 1

        return longest