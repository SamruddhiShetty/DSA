#here a given number X and power N , we have to find the total number of ways we can get the value x by adding set of natural 
#numbers (1, 2, 3....) raised to power N. Eg:- X=10 N=2, sum=1^2+3^2=10, hence only one way, ans=1.

import math
import os

# Complete the powerSum function below.
def deconstruct(X, N, l, i, f):
    val=l[i]**N
    if val>X:
        return 0
    elif X-val==0:
        return 1
    else:
        if i+1<f:
            return deconstruct(X-val, N, l, i+1, f) + deconstruct(X, N, l, i+1, f)
        else:
            return 0


def powerSum(X, N):
    size=math.floor(X**(1/N))
    l=[]
    for i in range(1, size+1):
        l.append(i)
    print(l)
    return deconstruct(X, N, l, 0, len(l))
    

if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    X = int(input())

    N = int(input())

    result = powerSum(X, N)
    print(result)

   # fptr.write(str(result) + '\n')

    #fptr.close()
