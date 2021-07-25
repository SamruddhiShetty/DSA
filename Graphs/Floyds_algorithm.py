#in both the cases the time efficiency is theta(n^3)
#space efficiency is O(n^2)
#its basically the application of dynamic programing on graphs
#this algorithm finds shortest paths from one vertex to all other vertex

#case 1: when the weights are positive i.e the graph is without any negative cycle
import sys

class Edge:
    def __init__(self, src, dest, wt):
        self.src=src
        self.dest=dest
        self.wt=wt

class Graph:
    def __init__(self, N):
        self.adj=[[sys.maxsize for i in range(N)] for j in range(N)]

        for i in range(N):
            self.adj[i][i]=0

    def connect(self, edges):
        for i in edges:
            self.adj[i.src][i.dest]=i.wt
        return self.adj

    def warshall(self, N):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    self.adj[i][j]=min(self.adj[i][j], self.adj[i][k]+self.adj[k][j])

        return self.adj


if __name__=="__main__":
    edges=[Edge(1, 0, 2), Edge(0, 2, 3), Edge(2, 1, 7), Edge(2, 3, 1), Edge(3, 0, 6)]

    x=Graph(4)
    print(x.connect(edges))
    print(x.warshall(4))
    
    
#case 2: when the graph has negative weights or negative cycle: (this contains only the logic)
def shortest_distance(self, matrix):
		#Code here
		N=len(matrix)
		
		for k in range(N):
		    for i in range(N):
		        for j in range(N):
		            if matrix[i][k]==-1 or matrix[k][j]==-1:
		                continue
		            elif matrix[i][j]==-1:
		                matrix[i][j]=matrix[i][k]+matrix[k][j]
		            else:
		                matrix[i][j]=min(matrix[i][j], matrix[i][k]+matrix[k][j])
		return
