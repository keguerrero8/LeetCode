# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        if head.next is None:
            return head
            
        slow, end = head, head
        count = 1
        while end.next:
            end = end.next
            count += 1

        midCount = 1
        while midCount < (count // 2):
            slow = slow.next
            midCount += 1

        self.reverseList(slow.next)
        slow.next = None

        start = head

        while count > 0:
            if count == 1:
                break
            if start.val != end.val:
                return False
            count -= 2
            start = start.next
            end = end.next

        return True


    def reverseList(self, node):
        p1 = None
        p2 = node

        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
        