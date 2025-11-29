# Last updated: 11/29/2025, 1:06:54 AM
1class Solution:
2    def validPalindrome(self, s: str) -> bool:
3        def is_pal(l: int, r: int) -> bool:
4            # 判断 s[l:r+1] 是否是回文
5            while l < r:
6                if s[l] != s[r]:
7                    return False
8                l += 1
9                r -= 1
10            return True
11
12        l, r = 0, len(s) - 1
13
14        while l < r:
15            if s[l] == s[r]:
16                l += 1
17                r -= 1
18            else:
19                # 删除一次：要么删左边，要么删右边
20                return is_pal(l + 1, r) or is_pal(l, r - 1)
21
22        return True
23