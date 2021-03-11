#the leader elements are the ones whoes right side elements are always less than itself

def findLeader(l):
    a=[]
    currLeader=l[-1]
    a.append(l[-1])
    for i in range(len(l)-2, -1, -1):
        if l[i]>a[-1]:
            currLeader=l[i]
            a.append(l[i])
        else:
            continue      
    a.reverse()
    return a


if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    
    print(findLeader(l))
    
    
#time complexity O(n)
#pace complexity O(1)
