# Last updated: 12/3/2025, 8:54:39 PM
1class Solution:
2    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
3        
4        seen = set()
5        l = 0
6        
7        for i in range(len(nums)):
8            if i - l > k:
9                seen.remove(nums[l])
10                l +=1
11            
12            if nums[i] in seen:
13                return True
14            
15            seen.add(nums[i])
16        return False
17