#return the max stops which can be provided to the trains where their (arrival time, departure time, platform_no) is given
#we have to find the number of trains which can be allowed on each platform
#this method is similar to activity_search problem
from collections import defaultdict
import sys

def maxTrain(arr):
    dicti=defaultdict(list)
    for i in arr:
        dicti[i[2]].append((i[0], i[1]))
        
    print(dicti)
    
    for j in dicti:
        dicti[j].sort(key=lambda x:x[1])
    print(dicti)
    
    count=0
    
    for i in dicti:
        current_time=-(sys.maxsize-1)
        for j in dicti[i]:
            if j[0]>=current_time:
                count+=1
                current_time=j[1]
            else:
                pass
            
        
        
    return count

if __name__=="__main__":
    arr=[[1000, 1030, 1], [1010, 1030, 1], [1000, 1020, 2], [1030, 1230, 2], [1200, 1230, 3], [900, 1005, 1]]
    print(maxTrain(arr))
