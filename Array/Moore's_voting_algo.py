#here we are supposed to find the elements with the majority count i.e. 
#where the number of occurence of the element should be more than half of the size of the whole array.

def majorityElement(l):
    res=0
    count=1
    for i in range(1, len(l)):
        if l[i]==l[res]:
            count +=1
        else:
            count -=1
        
        if count==0:
            res=i
            count=1
            
    count=0
    for i in range(0, len(l)):
        if l[res]==l[i]:
            count+=1
    if count<=(len(l)//2):
        return -1
    return res
    


if __name__=="__main__":
    print("Enter the array")
    l=list(map(int, input().strip().split()))
    print(majorityElement(l))
