# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        slow, right = head, head
        
        count = 1
        while right.next:
            count += 1
            right = right.next
        
        if count == 1:
            return head
            
        slowCount = 1   
        while slowCount < count // 2:
            slowCount += 1
            slow = slow.next
            
        self.reverseList(slow.next)
        slow.next = None
        
        newList = newListHead = ListNode(None)
        left = head
        #1 -> 2 -> None'
        #5 -> 4 -> 3 -> None'
        #None -> 1 -> 5 -> 2 -> 4 -> 3
        while left or right:
            if left:
                newList.next = left
                newList = newList.next
                left = left.next
            newList.next = right
            newList = newList.next
            right = right.next
            
        return newListHead.next
        
        
        
    def reverseList(self, node):
        p1 = None
        p2 = node
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3