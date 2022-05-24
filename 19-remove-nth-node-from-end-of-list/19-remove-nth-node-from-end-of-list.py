# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    #1 -> None, n = 1

    def removeNthFromEnd(self, head, n):
        slow = fast = head
        counter = 1
        while counter < n+2:
            if fast is not None:
                fast = fast.next
            else:
                break
            counter += 1
        
        while fast:
            fast = fast.next
            slow = slow.next
            
        if counter == n+2:
            slow.next = slow.next.next
        else:
            head = head.next
        return head
        
        
            
        