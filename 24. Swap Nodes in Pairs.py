# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        new=ListNode(next=head)
        pointer=new

        while pointer and pointer.next and pointer.next.next:
            slow=pointer.next
            fast=pointer.next.next
            pointer.next=fast
            slow.next=fast.next
            fast.next=slow
            pointer=slow
        return new.next
            

            




        

        

        