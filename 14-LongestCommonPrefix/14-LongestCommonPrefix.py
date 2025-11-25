# Last updated: 11/25/2025, 1:17:29 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            ch = first[i]
            for s in strs:
                if i == len(s) or ch != s[i]:
                    return first[:i]
        return first