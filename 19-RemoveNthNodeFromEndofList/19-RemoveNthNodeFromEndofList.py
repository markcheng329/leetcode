# Last updated: 1/4/2026, 7:55:24 PM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8
9        dummy = ListNode(0,head)
10        tail = dummy
11
12        slow,fast = tail,tail
13
14        for i in range(n+1):
15            fast = fast.next
16        
17        while fast:
18            slow = slow.next
19            fast = fast.next
20        
21        slow.next = slow.next.next
22
23        return dummy.next
24
25