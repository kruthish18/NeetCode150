# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def height(root):
            if root is None:
                return 0
            
            left = self.height(root.left)
            right = self.height(root.right)

            if left < 0 or right < 0:
                return -1
            
            if abs(left-right)>1:
                return -1
            
            return 1+max(left,right)
        
        return height(root) >= 0


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(log n) for balanced trees (average case) , O(n) for skewed trees (worst case)