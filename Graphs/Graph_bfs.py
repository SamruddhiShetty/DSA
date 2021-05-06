from queue import Queue
class Solution:
    
    #Function to return Breadth First Traversal of given graph.
    def bfsOfGraph(self, V, adj):
        # code here
        q=Queue(maxsize=0)
        l=[False]*V
        result=[]
            
        q.put(0)
        l[0]=True
        
        while (q.empty()==False):
            vertex=q.get()
            
            result.append(vertex)
            
            for j in adj[vertex]:
                if l[j]==False:
                    q.put(j)
                    l[j]=True
                    
        return result
      
     
if __name__=="__main__":
  T=int(input())  #test cases
  for i in range(T):
    V, E=map(int, input().split())
    adj=[[] for i in range(V)]
    for _ in range(E):
      u, v=map(int, input().split())
      adj[u].append(v)
      ob=Solution()
      ans=ob.bfsOfGraph(adj, V)
      for i in range(len(ans)):
        print(ans[i], end=" ")
       print()
