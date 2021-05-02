#the problem gives three arrays(house number and diameter of the pipe) a-> house with outgoing pipe, b-> house with incoming pipe, d-> diameter of the pipe from the house
#we have to find a way to connect all the house with incoming pipe to the house with outgoing pipe
#dfs is the main logic
#just try to remember the way to solve

ans=0
class Solution:
    def __init__(self):
        self.cd=[0]*1100 #incoming line
        self.rd=[0]*1100 #outgoing line
        self.wt=[0]*1100
    
    def dfs(self, j):
        global ans
        if self.cd[j]==0:
            return j
        ans=min(ans, self.wt[j])
        return self.dfs(self.cd[j])
    def solve(self, n, p ,a, b, d): 
        #code here
        #a is the array which shows the array of house numbers with tank
        #b is the array with house  number with taps
        
        
        for i in range(p):
            x=a[i]
            y=b[i]
            z=d[i]
            
            self.cd[x]=y
            self.wt[x]=z
            self.rd[y]=x
            
        m=[]
        q=[]
        o=[]
        global ans
        for j in range(1, (n+1)):
            if (self.rd[j]==0 and self.cd[j]):
                
                ans=10**7
                w=self.dfs(j)
                m.append(j)
                q.append(w)
                o.append(ans)
                
        result=[]
        for i in range(len(m)):
            result.append((m[i], q[i], o[i]))
        return result
