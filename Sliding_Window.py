#this fruit into basket the problem basically states that there are different type of trees in a row and we have 2 baskets which are meant to carry only two distinct types
#of fruits so we are supposed to return the max number of fruits we could collect so far considering that we can have only two types of fruits.

class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        a, b, na, nb, j, res=-1, -1, 0, 0, 0, 0  #a-secondLast b-last fruit
        #na- no. of a type fruit nb- no.of b type fruit j- pointer which points the last fruit which was considered
        
        for i in tree:
            if i==b:
                nb+=1
            elif i==a:
                na+=1
                a, b=b, a
                na, nb=nb, na
            else:
                while na:  #deduct the count of both the fruits until the point where we have only 2 different fruits in consideration
                    y=tree[j]
                    if y==a:
                        na-=1
                    else:
                        nb-=1   #this makes sure that the last element which was interleaved between the fruit which is currently getting eliminated, will also be 
                    j+=1         #taken off the basket this will make sense if u make a dry run with ur own exalmple
                a, b=b, i
                na, nb=nb, 1
            if res<(na+nb):  #every iteration we are updating the result so that it contains the maximum number of fruits so far
                res=na+nb
                
        return res
