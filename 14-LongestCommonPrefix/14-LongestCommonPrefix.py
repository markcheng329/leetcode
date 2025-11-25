# Last updated: 11/25/2025, 1:05:47 AM
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first = strs[0]

        for i in range(len(first)):
            ch = first[i]
            for s in strs[1:]:
                if i == len(s) or ch != s[i]:
                    return first[:i]
        return first