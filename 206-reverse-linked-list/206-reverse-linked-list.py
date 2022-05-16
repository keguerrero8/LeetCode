# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        if head is None:
            return head
        
        p1 = None
        p2 = head
        p3 = p2.next
        p2.next = None
        
        while p3:
            p1 = p2
            p2 = p3
            p3 = p3.next
            p2.next = p1
            
        return p2