# Last updated: 1/5/2026, 2:50:18 AM
1class Solution:
2    def findDuplicate(self, nums: List[int]) -> int:
3        slow = nums[0]
4        fast = nums[nums[0]]
5
6        while slow != fast:
7            slow = nums[slow]
8            fast = nums[nums[fast]]
9        
10        res = 0
11
12        while res != slow:
13            res = nums[res]
14            slow = nums[slow]
15        
16        return res