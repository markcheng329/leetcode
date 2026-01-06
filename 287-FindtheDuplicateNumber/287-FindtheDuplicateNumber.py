# Last updated: 1/6/2026, 1:44:19 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow = nums[0]
4        fast = nums[nums[0]]
5
6        while slow!=fast:
7            slow = nums[slow]
8            fast = nums[nums[fast]]
9
10        slow2 = 0
11
12        while slow2 !=slow:
13            slow = nums[slow]
14            slow2 = nums[slow2]
15        
16        return slow2
17        