# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        if head is None or head.next is None:
            return head
            
        
        leftHead = ListNode(None)
        left = leftHead
        rightHead = ListNode(None)
        right = rightHead
        current = head
        
        while current:
            if current.val < x:
                left.next = current
                left = left.next
            else:
                right.next = current
                right = right.next
            current = current.next
            
        left.next = rightHead.next if right.val is not None else None 
        right.next = None
        
        return leftHead.next
        