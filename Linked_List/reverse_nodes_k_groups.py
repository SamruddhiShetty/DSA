class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head.next==None or k==1:
            return head
        dummy=head
        count=0
        while dummy and count<k:
            count+=1
            dummy=dummy.next
            
        if count==k:
            current=head
            prev=after=None

            while current!=dummy:
                after=current.next
                current.next=prev
                prev=current
                current=after
        
            if current!=None:
                head.next=self.reverseKGroup(current, k)
            return prev
        else:
            return head
        
        
