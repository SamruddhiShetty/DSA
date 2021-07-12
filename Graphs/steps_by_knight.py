#time complexity is O(n)^2  at the wordt case all the cells will be visited hence n^2
#space complexity is O(n)^2
#it uses graphs bfs method 

#refer the problem from here https://practice.geeksforgeeks.org/problems/steps-by-knight5927/1#

def minStepToReachTarget(self, KnightPos, TargetPos, N):
	    def isValid(i, j):
            if i <= 0 or i > N or j <= 0 or j > N:
                return False
            return True
        queue = [[KnightPos[0], KnightPos[1]]]
        visited = [[0]*(N+1) for _ in range(N+1)]
        moves = [[2, -1],[2, 1],[-2,-1],[-2,1],[-1,-2],[-1,2],[1,-2],[1,2]]
        dist = [[0]*(N+1) for _ in range(N+1)]
        visited[KnightPos[0]][KnightPos[1]] = 1
        while(queue):
            x = queue.pop(0)
            if x[0] == TargetPos[0] and x[1] == TargetPos[1]:
                return dist[x[0]][x[1]]
            for i in moves:
                if isValid(x[0]+i[0], x[1]+i[1]) and not visited[x[0]+i[0]][x[1]+i[1]]:
                    queue.append([x[0]+i[0], x[1]+i[1]])
                    dist[x[0]+i[0]][x[1]+i[1]] = dist[x[0]][x[1]] + 1
                    visited[x[0]+i[0]][x[1]+i[1]] = 1
        return dist[x[0]][x[1]]
