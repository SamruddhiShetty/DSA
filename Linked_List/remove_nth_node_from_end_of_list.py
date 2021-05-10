#if the given number is 4 remove 4th node from the end
#this has to be done in one pass

#hence we use a slow and a fast pointer where the fast pointer will be (n+1) ahead of slow that is if slow points at 1st node fast points at (n+1)th node

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy=ListNode()
        dummy.next=head
        left=dummy
        right=head
        
        count=0
        while right:
            count+=1
            if count>n:
                left=left.next
            right=right.next
            
        left.next=None if not left.next else left.next.next

        #this is used just to ensure that the right head is sent back to the answer if incase the head itself was eliminated
        return dummy.next
