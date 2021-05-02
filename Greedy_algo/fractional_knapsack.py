#we will have to find the max value possible wherein we can have (0-1) fraction of each item- 0, 1 are inclusive
#so we sort a array with the ratio of Value/Weight and we take the original index to reach every item in the given two arrays-weight and value

def fractionalknapsack(self, W,Items,n):
        
        # code here
        fraction=[]
        for i in range(n):
            fraction.append((i, (Items[i].value/Items[i].weight)))
            
        fraction.sort(key=lambda x:x[1], reverse=True)
        
        result=0
        for i in fraction:
          #considering the elements with weight less than or equal to the remaining capaciity of the knapsack 
            if (W-Items[i[0]].weight)>=0:
                result+=Items[i[0]].value
                W=W-Items[i[0]].weight
          #this will run only once either when the capacity is already achieved or when there is a item whoes weight is more than the present capacity
            else:
                fraction=W/Items[i[0]].weight
                z=Items[i[0]].value*fraction
                result+=z
                break
            
            
        return result
