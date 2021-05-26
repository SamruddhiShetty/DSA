from collections import deque

#refer the questinon from https://practice.geeksforgeeks.org/problems/connect-nodes-at-same-level/1#
#here i used the bfs traversal and two pointers we connect the nodes at the same level only if the prev is pointing to a node before the current
class Solution:
    #Function to connect nodes at same level.
    def connect(self, root):
        q=deque()
        q.append(root)
        
        temp=Node(None)
        while q:
            n=len(q) #here the list will have all nodes from each level
            for i in range(n):  #here we are iterating over each level
                prev=temp
                temp=q.popleft()
                
                if (i>0):  #this is done to avoid connecting the last node from the previous level and just connecting the nodes from the same level 
                    prev.nextRight=temp
                    
                if temp.left:
                    q.append(temp.left)
                    
                if temp.right:
                    q.append(temp.right)
                    
            temp.nextRight=None      #the last node from each level is connected to the None
            
        return root
