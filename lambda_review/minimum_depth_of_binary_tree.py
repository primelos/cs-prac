"""Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        print(root.left.val)
        if root == None:
            return 0

        queue = [(root, 1)]
        while len(queue) > 0:
            cur = queue.pop(0)
            cur_node, cur_level = cur[0], cur[1]
            if cur_node.left == None and cur_node.right == None:
                return cur_level
            elif cur_node.left != None:
                queue.append((cur_node.left , cur_level + 1))
            elif cur_node.right != None:
                queue.append((cur_node.right, cur_level + 1))

        return -1

a = TreeNode(3) # ROOT
b = TreeNode(9)
c = TreeNode(20)
d = TreeNode(15)
e = TreeNode(7)
a.left = b
a.right = c
c.left = d
c.right = e

test1 = Solution()
print(test1.minDepth(a))
