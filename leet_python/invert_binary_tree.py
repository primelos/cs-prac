Invert a binary tree.

Example:

Input:

     4
   /   \
  2     7
 / \   / \
1   3 6   9
Output:

     4
   /   \
  7     2
 / \   / \
9   6 3   1

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# [4,2,7,1,3,6,9] given
# [4,7,2,9,6,3,1] goal
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:

        a = root 
        if a is None:
            return
        self.invertTree(a.left)
        self.invertTree(a.right)
        a.left, a.right = a.right, a.left

        return a
        
#       OR CALL A FUNCTION
#         def dfs(node):
#             if node is None:
#                 return 
#             dfs(node.left)
#             dfs(node.right)
            
#             node.left, node.right = node.right, node.left
        
#         dfs(root)
#         return root