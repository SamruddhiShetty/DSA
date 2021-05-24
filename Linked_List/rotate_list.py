#the usage of two pointers one to point the last element and also to get the length of the list and the other pointer to point the element whoes next element till the 
#end has to be transfered to the front

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head==None or head.next==None:
            return head
            
        count=1
        left=head
        right=head
        
        #one pass to count the length of the list
        while right.next!=None:
            right=right.next
            count+=1
        
        rotate=count-(k%count) #point from head whoes next element onward has to be transfered to the front
        if (k%count)==0:
            return head
        
        current=head
        dummy=1
        while dummy!=rotate:  #this is to reach till that element
            current=current.next
            dummy+=1
        right.next=head
        head=current.next
        current.next=None
        return head
