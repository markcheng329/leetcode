# Last updated: 11/12/2025, 4:58:53 AM
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        lens = {len(w) for w in words}
        n = len(s)
        dp = [False]*(n+1)
        dp[0] = True
        for i in range(1, n+1):
            for L in lens:
                j = i - L
                if j >= 0 and dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[n]