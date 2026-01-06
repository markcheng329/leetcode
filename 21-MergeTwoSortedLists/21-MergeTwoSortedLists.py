# Last updated: 1/6/2026, 12:45:07 AM
1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
8        dummy = ListNode()
9        tail = dummy
10
11        while list1 and list2:
12            if list1.val > list2.val:
13                tail.next = list2
14                list2 = list2.next
15            else:
16                tail.next = list1
17                list1 = list1.next
18            tail = tail.next
19        
20        tail.next = list1 or list2
21
22        return dummy.next