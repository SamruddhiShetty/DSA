#refer the problem from here https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

#time= O(n)
#space=O(n)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def helper(self, preStart, inStart, inEnd, preorder, inorder):
        if preStart>len(preorder)-1 or inStart>inEnd:
            return None
        rootIndex=0
        for i in range(inStart, inEnd+1):
            if inorder[i]==preorder[preStart]:
                rootIndex=i
                break
                
        root=TreeNode(preorder[preStart])
        
        root.left=self.helper(preStart+1, inStart, rootIndex-1, preorder, inorder)
        root.right=self.helper(preStart+rootIndex-inStart+1, rootIndex+1, inEnd, preorder, inorder)
        
        return root
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(0, 0, len(inorder)-1, preorder, inorder)
      
      (or)
      
      
     class Solution:
    
    def helper(self, preStart, inStart, inEnd, preorder, Dict):
        rootIndex=Dict[preorder[preStart]]
                
        root=TreeNode(preorder[preStart])
        
        if inStart<rootIndex:
            root.left=self.helper(preStart+1, inStart, rootIndex-1, preorder, Dict)
            
        if rootIndex<inEnd:
            root.right=self.helper(preStart+rootIndex-inStart+1, rootIndex+1, inEnd, preorder, Dict)
        
        return root
            
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        Dict={inorder[i]:i for i in range(len(inorder))}
        return self.helper(0, 0, len(inorder)-1, preorder, Dict)
      
      
