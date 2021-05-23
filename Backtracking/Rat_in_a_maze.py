#refer the problem from here https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1

#here m- given square matrix and n is the size of row and column

class Solution:
    def __init__(self):
        self.possiblePaths=[]
    def isSafe(self, x, y, n, m, visited):
        if x<0 or x>=n or y<0 or y>=n or m[x][y]==0 or visited[x][y]==1:
            return False
        return True
        
    def backtracking(self, x, y, n, m, visited, paths):
        
        #base condition 1
        if not self.isSafe(x, y, n, m, visited): #this takes care of the condition when the first element is 0 
            return        
        
        #base condition 2
        if x==n-1 and y==n-1:
            self.possiblePaths.append(paths)
            return
        
        visited[x][y]=1
        
        #follow the same order to get the answer lexicographically
        if self.isSafe(x+1, y, n, m, visited):
            paths+='D'
            self.backtracking(x+1, y, n, m, visited, paths)
            paths=paths[:-1]  #this is used to eliminate the current character after
                              #we have tried every possible direction from here            
        if self.isSafe(x, y-1, n, m, visited):
            paths+='L'
            self.backtracking(x, y-1, n, m, visited, paths)
            paths=paths[:-1]
            
        if self.isSafe(x, y+1, n, m, visited):
            paths+='R'
            self.backtracking(x, y+1, n, m, visited, paths)
            paths=paths[:-1]
            
        if self.isSafe(x-1, y, n, m, visited):
            paths+='U'
            self.backtracking(x-1, y, n, m, visited, paths)
            paths=paths[:-1]
            
        visited[x][y]=0  #once u have tried every nook and corner from here mark it as unvisited
    def findPath(self, m, n):
        # code here
        
        visited=[[0 for i in range(n)] for j in range(n)]
        paths=""
        self.backtracking(0, 0, n, m, visited, paths)
        return self.possiblePaths
