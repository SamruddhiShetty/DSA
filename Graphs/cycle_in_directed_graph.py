class Solution:
    
    #Function to detect cycle in a directed graph.
    def CyclicUnit(self, v, visited, recStack, adj):
        visited[v]=True
        recStack[v]=True #this is used to keep track of all the elements belonging to a single subtree of the whole graph
        
        for j in adj[v]:
            if visited[j]==False:
                if self.CyclicUnit(j, visited, recStack, adj)==True:
                    return True
            elif recStack[j]==True:  #if the vertex is already visited check whether it is present in the recursion stack only then we can predict the cyclicity
                return True
            
        recStack[v]=False    #after completing the dfs travel and reaching the end of that subtree we remove all the elements from recStack by setting it False
        return False
    def isCyclic(self, V, adj):
        # code here
        visited=[False]*V
        recStack=[False]*V
        
        for i in range(V):
            if visited[i]==False:
                if self.CyclicUnit(i, visited, recStack, adj)==True:
                    return True
        return False
    
import sys
sys.setrecursionlimit(10**6)

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        V, E=list(map(int, input().strip().split()))
        adj=[[] for i in range(V)]
        for i in range(E):
            a, b=map(int, input().strip().split())
            adj[a].append(b)
        ob=Solution()
        
        if ob.isCyclic(V, adj):
            print(1)
        else:
            print(0)

 #time complexity is V+E
#space complexity is V (visited array)
