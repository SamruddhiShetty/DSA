#kind of AVL tree

class Solution:
    
    value=True
     
    def checkLength(self, root):
            if not root or not self.value:
                return 0
            left=self.checkLength(root.left)
            right=self.checkLength(root.right)
            if abs(left-right)>1:
                self.value=False
            return max(left, right)+1
        
    def isBalanced(self, root: TreeNode) -> bool:
        
        self.checkLength(root)
        return self.value
