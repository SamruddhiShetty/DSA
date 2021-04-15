#done using DFS..

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack=[(root, float('-inf'),float('inf') ), ]
        
        while stack:
            root, mini, maxi=stack.pop()
            if not root:
                continue
            if root.val<=mini or root.val>=maxi:
                return False
            stack.append((root.left, mini, root.val))
            stack.append((root.right, root.val, maxi))
        return True
        
 # time complexity is O(N) in the worst case when it is BST or the wrong node is the rigthmost node.
 #space comlexity is O(N).
