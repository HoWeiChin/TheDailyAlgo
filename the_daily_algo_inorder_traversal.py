import sys
class Solution(object):
    def InorderTraversal(self, root, res):
        if root is None:
            return
        self.InorderTraversal(root.left, res)
        res.append(root.val)
        self.InorderTraversal(root.right, res)
        
        return
        
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = []
        self.InorderTraversal(root, res)
        
        minDiff = sys.maxsize
        
        for i in range(len(res)):
            if i == len(res) - 1:
                break
            
            diff = abs(res[i] - res[i+1])
            minDiff = min(diff, minDiff)
        
        return minDiff
