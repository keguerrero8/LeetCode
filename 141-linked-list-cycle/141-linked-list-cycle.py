# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next is not None else None
            if fast is None:
                return False
            if slow.val == fast.val and slow.next == fast.next:
                return True
            
        return False
    