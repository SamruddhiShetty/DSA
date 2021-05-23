class Solution:
    
    #Function to detect cycle in an undirected graph.
    def cyclicUnit(self, v, visited, adj, parent):
        visited[v]=True
        
        for j in adj[v]:
            if visited[j]==False:
                if self.cyclicUnit(j, visited, adj, v):
                    return True
            elif parent!=j:     #if the vertex is already visited then we just check whether it is the immediate parent of the current node if it is then it is not cylcic
                return True     #this has to be taken care only in undirected graph, but if it is not the parent and still visited then it is cyclic
                
        return False
	def isCycle(self, V, adj):
		#Code here
		visited=[False]*V
		
		for i in range(V):
		    if visited[i]==False:
		        if self.cyclicUnit(i, visited, adj, -1):
		            return True

#time complexity is V+E
#space complexity is V (visited array)
