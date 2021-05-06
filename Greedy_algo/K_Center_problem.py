def findmax(dist, n):
    mi=0
    for i in range(n):
        if dist[i]>dist[mi]:
            mi=i
    return mi

def selectKcities(weights, n, k):
    dist=[10**9]*n
    centers=[]
    
    maxi=0
    for i in range(k):
        centers.append(maxi)
        
        for j in range(n):
            dist[j]=min(dist[j], weights[maxi][j])
        maxi=findmax(dist, n)
        
    print(dist[maxi])
    for i in centers:
        print(i, end=" ")
        

if __name__=="__main__":
    n=4
    
    k=2
    
    weights=[ [ 0, 4, 8, 5 ],
              [ 4, 0, 10, 7 ],
              [ 8, 10, 0, 9 ],
              [ 5, 7, 9, 0 ] ]
    selectKcities(weights, n, k)
