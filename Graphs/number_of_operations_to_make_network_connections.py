#refer problem from here https://leetcode.com/problems/number-of-operations-to-make-network-connected/
#this is using DFS 
#run time= O(V+E)

from collections import defaultdict
class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections)<n-1:
            return -1
        visited=set()
        result=0
        
        graph=defaultdict(list)
        for i in range(n):
            graph[i].append(i)
        for i in connections:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])
            
        stack=[]
        for i in graph.keys():
            if i not in visited:
                result+=1
                visited.add(i)
                stack.append(i)
                while stack:
                    y=stack.pop()
                    for j in graph[y]:
                        if j not in visited:
                            visited.add(j)
                            stack.append(j)
                                        
                    
        return result-1
            
        
