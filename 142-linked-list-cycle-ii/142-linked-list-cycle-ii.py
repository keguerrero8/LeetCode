# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return None
        slow, fast = head, head

        while True:
            if fast.next and fast.next.next:
                fast = fast.next.next
            else:
                return None
            slow = slow.next
            if slow == fast:
                break

        new = head

        while new != slow:
            new = new.next
            slow = slow.next

        return slow
        