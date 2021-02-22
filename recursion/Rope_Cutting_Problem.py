#given a rope of length "length" and we have to get the maximum pieces after croping the rope according to the three given fixed lengths
#if its possible we have to return the possible max number of pieces else return it is impossible by returning "-1"

def cutRope(length, l1, l2, l3):
    if length==0:
        return 0
    elif length<0:
        return -1
    else:
        m1=cutRope(length-l1, l1, l2, l3)
        m2=cutRope(length-l2, l1, l2, l3)
        m3=cutRope(length-l3, l1, l2, l3)
        value=max(m1, m2, m3)
        
        #this is required to get the correct value else this function will always return a valid value.
        if value==-1:
            return -1
        else:
            return value+1

if __name__=="__main__":
    print("Enter the lenght of the Rope")
    length=int(input())
    print("Enter the three different lengths by which the rope is supposed to be cropped")
    l1=int(input())
    l2=int(input())
    l3=int(input())
    
    maxPiece=cutRope(length, l1, l2, l3)
    print(maxPiece)
