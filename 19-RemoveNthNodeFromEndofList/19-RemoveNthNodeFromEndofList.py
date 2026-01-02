# Last updated: 1/2/2026, 6:44:45 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = ListNode(0,head)
9        tail = dummy
10
11        fast,slow = tail,tail
12
13        for i in range(n+1):
14            fast = fast.next
15        
16        while fast:
17            fast = fast.next
18            slow = slow.next
19        
20        slow.next = slow.next.next
21
22        return dummy.next
23    