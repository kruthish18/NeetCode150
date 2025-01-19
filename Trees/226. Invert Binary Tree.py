class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        if root is None:
            return None

        temp = root.left
        root.left = root.right
        root.right = temp

        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


#Time & Space Complexity 
#Time complexity: O(n) 
#Space complexity: O(log n) for balanced trees (average case) , O(n) for skewed trees (worst case)