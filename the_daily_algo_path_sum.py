
def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
    if root is None:
        return 0
        
    if root.left is None and root.right is None and sum-root.val == 0:
        return True
        
    if root.left is None and root.right is None and sum-root.val != 0:
        return False
        
    left_has_path = self.hasPathSum(root.left, sum-root.val)
    right_has_path = self.hasPathSum(root.right, sum-root.val)
    
    if left_has_path or right_has_path:
        return True
    
    return False
        
