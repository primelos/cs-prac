# Merge two sorted linked lists and return it as a new sorted list. 
# The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return str(self.val)

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # Recursive Solution
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        
        if l1.val <= l2.val:
            head = l1
            head.next = self.mergeTwoLists(l1.next, l2)

        else:
            head = l2
            head.next = self.mergeTwoLists(l1, l2.next)
        return head

        # Iterative solution
        '''
        l3 = l4 = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                l4.next = l1
                l1 = l1.next
            else:
                l4.next = l2
                l2 = l2.next
            l4 = l4.next 
            
        l4.next = l1 or l2
        return l3.next
        '''
l1 = ListNode(1)
la = ListNode(2)
l1.next = la
lb = ListNode(4)
la.next = lb

l2 = ListNode(1)
lc = ListNode(3)
l2.next = lc
ld = ListNode(4)
lc.next = ld
# print(l1.next)

ss = Solution()
print(ss.mergeTwoLists(l1,l2))
