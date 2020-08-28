# You are given two non-empty linked lists representing two non-negative 
# integers. The digits are stored in reverse order and each of their nodes 
# contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except 
# the number 0 itself.

# Example:
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __str__(self):
        return str(self.val)
    
class Solution:
    def __init__(self):
        self.head = None
        
    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.val)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        temp, carry = None, 0
        node = prev = None
        while l1 is not None or l2 is not None:
            new_l1 = 0 if l1 is None else l1.val
            new_l2 = 0 if l2 is None else l2.val
            
            total = carry + new_l1 + new_l2
            
            carry = 1 if total >= 10 else 0
            
            total = total if total < 10 else total % 10
            
            temp = ListNode(total)
            
            
            if node is None:
                node = temp
            else:
                prev.next = temp
            prev = temp
        
            if l1 is not None:
                l1 = l1.next
                
            if l2 is not None:
                l2 = l2.next

        if carry:
            prev.next = ListNode(carry)
        return node
    def printIt(self):
        while node:
            print(node.val)
# class Solution:
#     def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
#         temp1 = ''
#         temp2 = ''

#         while l1:
#             temp1 += str(l1.val)
#             l1 = l1.next
  
#         while l2:
#             temp2 += str(l2.val)
#             l2 = l2.next
        
#         new_l1 = int(temp1[::-1])
#         new_l2 = int(temp2[::-1])
        
#         reverse = list(map(int, str(new_l1 + new_l2)[::-1] ))
#         print(type(reverse))
#         head = node = None
#         for i in reverse:
#             print('i',i)
            
#             llist = ListNode(i)
#             print(llist)
#             if node is not None: 
#                 node.next = llist #<-- not none-runs this code after the 1st iteratio
#             node = llist # <--- is none runs the first time
#             if head is None:  
#                 head = node  #<-- is none give me the starting point runs once
                
#         print('head',head)
#         return head




a = ListNode(2)
b = ListNode(4)
a.next = b
c = ListNode(3)
b.next = c

x = ListNode(5)
y = ListNode(6)
x.next = y
z = ListNode(4)
y.next = z

test1 = Solution()
print(test1.addTwoNumbers(a, x))
print(test1)