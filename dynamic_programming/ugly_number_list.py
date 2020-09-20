#Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
#The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, … shows the first 11 ugly numbers. By convention, 1 is included. 
class Solution:
    def getNthUglyNo(self,n):
        ugly_array=[1]
        i2=i3=i5=0
        for i in range(1, n):
            multi2=ugly_array[i2]*2
            multi3=ugly_array[i3]*3
            multi5=ugly_array[i5]*5
            x=min(multi2, multi3, multi5)
            if x==multi2:
                i2 +=1
            if x==multi3:
                i3 +=1
            if x==multi5:
                i5 +=1
            ugly_array.append(x)
        return ugly_array[-1]
