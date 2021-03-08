#Remove duplicates from sorted array


def removeDuplicates(l):
    res=1
    for i in range(1, len(l)):
        if l[i]!=l[res-1]:
            l[res]=l[i]
            res +=1
    return res
            

if __name__=="__main__":
    print("enter the array")
    l=list(map(int, input().strip().split()))
    print(removeDuplicates(l))
    
    
#auxillary space= O(1)
#time complexity= theta(n)
