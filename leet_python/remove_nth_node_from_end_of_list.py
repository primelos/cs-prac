# Given a linked list, remove the n-th node from the end of list and return its head.

# Example:

# Given linked list: 1->2->3->4->5, and n = 2.

# After removing the second node from the end, the linked list becomes 1->2->3->5.
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:

        for i in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            fast = fast.next
            slow = fast.next
        slow.next = slow.next.next
        return head

a = ListNode(1)
b = ListNode(2)
a.next = b
c = ListNode(3)
b.next = c
d = ListNode(4)
c.next = d
e = ListNode(5)

d.next = e