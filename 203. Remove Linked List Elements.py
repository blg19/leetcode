# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:

        new=ListNode(next=head)
        previous=new
        current= head

        while current:
            if current.val==val:
                previous.next=current.next
            else:
                previous=current
            current=current.next
        return new.next

        



        

        


        