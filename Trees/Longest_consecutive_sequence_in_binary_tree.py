#refer questions from https://practice.geeksforgeeks.org/problems/longest-consecutive-sequence-in-binary-tree/1# 

res=0
class Solution:
    # your task is to complete this function
    # function should print the top view of the binary tree
    # Note: You aren't required to print a new line after every test case
    
    def find(self, root, expected, currentVal):
        if not root:
            return 
        
        if root.data==expected:
            currentVal+=1
        else:
            currentVal=1
         
        global res   
        res=max(res, currentVal)
        
        self.find(root.left, root.data+1, currentVal)
        self.find(root.right, root.data+1, currentVal)
    def longestConsecutive(self, root):
        # Code here
        global res
        res=0
        if not root:
            return 0
        self.find(root, root.data, 0)
        if res==1:
            return -1
        else:
            return res
        
