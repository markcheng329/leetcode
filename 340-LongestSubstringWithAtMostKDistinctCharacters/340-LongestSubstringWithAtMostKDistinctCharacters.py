# Last updated: 11/12/2025, 4:57:46 AM
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        count = defaultdict(int)
        left = 0
        res = 0

        for i in range(len(s)):
            count[s[i]] +=1

            while len(count) > k:
                count[s[left]] -=1
                if count[s[left]] == 0:
                    del count[s[left]]
                left +=1
            
            res = max(res,i-left+1)
        return res