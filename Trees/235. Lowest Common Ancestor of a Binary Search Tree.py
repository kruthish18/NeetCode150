# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        if root is None:
            return None
        
        if p.val<root.val and q.val<root.val:
            root=root.left

        elif p.val>root.val and q.val>root.val:
            root=root.right

        else:
            return root


#Time & Space Complexity 
#Time complexity: O(h): Where h is the height of the tree. 
# The worst-case time complexity is determined by the height of the BST, as the while loop continues until it finds the LCA or reaches a leaf node. 
# In the worst-case scenario (a skewed tree), the height could be n (where n is the number of nodes in the tree), making the time complexity O(n). 
# In a balanced BST, the height would be approximately log n, and hence the time complexity would be O(log n).
#Space complexity: O(1)