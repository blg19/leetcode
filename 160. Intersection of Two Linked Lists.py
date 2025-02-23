# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        liste=set()
        a=headA
        b=headB

        while a:
            liste.add(a)
            a=a.next
        while b:
            if b in liste:
                return b
            b=b.next
        return None




        