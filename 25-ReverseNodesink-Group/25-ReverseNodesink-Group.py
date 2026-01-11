# Last updated: 1/11/2026, 6:29:37 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        dummy = ListNode(0,head)
9        groupprev = dummy
10
11        while True:
12            kth = self.getk(groupprev,k)
13            if not kth:
14                break
15            
16            groupnext = kth.next
17            prev,cur = groupnext,groupprev.next
18            while cur != groupnext:
19                temp = cur.next
20                cur.next = prev
21                prev = cur
22                cur = temp
23            
24            temp = groupprev.next
25            groupprev.next = kth
26            groupprev = temp
27        return dummy.next
28    
29
30
31
32    def getk(self,cur,k):
33        while cur and k > 0:
34            cur = cur.next
35            k-=1
36        return cur
37