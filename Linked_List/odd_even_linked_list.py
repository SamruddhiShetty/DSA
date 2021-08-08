#refer the problem from here https://leetcode.com/problems/odd-even-linked-list
#space- O(1)
#runtime O(n)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        odd, beginEven, even=head, head.next, head.next
        
        if even==None or even.next==None:
            return head
        current=even.next
        
        while current:
            odd.next=current
            even.next=current.next
            current.next=beginEven
            
            even=even.next
            odd=odd.next
            if even:
                current=even.next
            else:
                current=None
        return head
        
