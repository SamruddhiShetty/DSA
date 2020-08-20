# Algorithms_examples

def getWays(n, c):
    # Write your code here
    c=sorted(c)
    ways=[0]*(n+1)
    ways[0]=1
    for i in c:
        for j in range(1, n+1):
            if i<=j:
                #getting the number of ways the other smaller elements are obtained after subtracting the present coin from the amount 
                ways[j]=ways[j-i]+ways[j]
            else:
                pass
    return ways[-1]
if __name__ == '__main__':
   # fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    first_multiple_input = input().rstrip().split()
    #this is the total amount to which we have to find the number of ways it can be obtained
    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])
    #list of denominations we have
    c = list(map(int, input().rstrip().split()))

    # Print the number of ways of making change for 'n' units using coins having the values given by 'c'

    ways = getWays(n, c)
    print(ways)
    #fptr.write(str(ways) + '\n')

    #fptr.close()
