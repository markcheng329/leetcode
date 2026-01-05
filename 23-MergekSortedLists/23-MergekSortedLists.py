# Last updated: 1/5/2026, 2:35:28 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
8        if len(lists) == 0:
9            return None
10        
11        if len(lists) == 1:
12            return lists[0]
13        
14        while len(lists) > 1:
15            res = []
16            for i in range(0,len(lists),2):
17                l1 = lists[i]
18                l2 = lists[i+1] if i+1 < len(lists) else None
19                res.append(self.mergeLists(l1,l2))
20            lists = res
21        return lists[0]
22
23    def mergeLists(self,l1,l2):
24        dummy = ListNode()
25        tail = dummy
26
27        while l1 and l2:
28            if l1.val > l2.val:
29                tail.next = l2
30                l2 = l2.next
31            else:
32                tail.next = l1
33                l1 = l1.next
34            tail = tail.next
35        
36        tail.next = l1 or l2
37
38        return dummy.next