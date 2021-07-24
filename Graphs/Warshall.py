#this is basically used to find transitive matrix
#the same logic is used for floyd's algorithm

#time efficiency is theta(n^3)
#space-- O(n^2)


#building directed graph
class Edge:
    def __init__(self, src, dest):
        self.src=src
        self.dest=dest

class Graph:
    def __init__(self, N):
        self.adj=[[0 for i in range(N)] for j in range(N)]

    def connect(self, edges):
        for i in edges:
            self.adj[i.src][i.dest]=1
        return self.adj

    def warshall(self, N):
        for k in range(N):
            for i in range(N):
                for j in range(N):
                    if self.adj[i][k]==1 and self.adj[k][j]==1:
                        self.adj[i][j]=1
                    else:
                        pass

        return self.adj


if __name__=="__main__":
    edges=[Edge(0, 1), Edge(1, 3), Edge(3, 0), Edge(3, 2)]

    x=Graph(4)
    print(x.connect(edges))
    print(x.warshall(4))
