#read the question from https://practice.geeksforgeeks.org/problems/mirror-tree/1#

#User function Template for python3

'''
class Node:
    def _init_(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
# your task is to complete this function
class Solution:
    #Function to convert a binary tree into its mirror tree.
    def mirror(self,root):
        # Code here
        current=root
        if root==None or (root.right==None and root.left==None):
            return root
        Right=self.mirror(root.left)
        Left=self.mirror(root.right)
        
        current.left=Left
        current.right=Right
        
        return current
      
  #time complexity is O(N), N- no.of nodes
  #space complexity is O(height of the tree)
