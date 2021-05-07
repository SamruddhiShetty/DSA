from collections import deque
class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def __init__(self):
        self.visited=[False]*V  #maintain a boolean list to keep in check the nodes
        #which are visited since graphs may have cycles hence the nodes may repeat
        #in graphs stack is not required but in trees it is required
        self.result=[] #the result list
        
        
    #in graphs to achieve dfs we need a recursive 
    function
    def dfs(self, adj, start):
        self.visited[start]=True
        self.result.append(start)
        
        for i in adj[start]:
            if self.visited[i]:
                continue
            else:
                self.dfs(adj, i)
