# Write a program to find the node at which the intersection of 
# two singly linked lists begins.
# For example, the following two linked lists:
# begin to intersect at node c1.

# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Reference of the node with value = 8
# Input Explanation: The intersected node's value is 8 (note that this must not be 
# 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From 
# the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected 
# node in A; There are 3 nodes before the intersected node in B.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
    def __repr__(self):
        return str(self.val)

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = headA
        b = headB
        
        while a != b:
            if a:
                a = a.next
               
            else:
                a = headB
                
            if b:
                b = b.next
                
            else:
                b = headA
               
        return a


a = ListNode(4)
b = ListNode(1)
c = ListNode(8)
d = ListNode(4)
e = ListNode(5)
a.next = b
b.next = c
c.next = d
d.next = e
e.next = None

a1 = ListNode(5)
b1 = ListNode(6)
c1 = ListNode(1)
d1 = ListNode(8)
e1 = ListNode(4)
f1 = ListNode(5)
a1.next = b1
b1.next = c1
c1.next = d1
d1.next = e1
e1.next = f1
f1.next = None

test1 = Solution()
print(test1.getIntersectionNode(a, a1))
print(a.next.next.next)