# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        end = head
        count = 1
        while end.next:
            end = end.next
            count += 1
        if count == 1:
            return head
        mid = (count // 2) 
        
        count = 1
        nodeToReverse = head
        while count < mid:
            nodeToReverse = nodeToReverse.next
            count += 1
            
        self.reverseList(nodeToReverse.next)
        nodeToReverse.next = None
        
        start = head
        new = newHead = ListNode(None)
        while start or end:
            if start:
                new.next = start
                start = start.next
                new = new.next
            new.next = end
            end = end.next
            new = new.next
            
        return newHead.next
        
        
        
    def reverseList(self, node):
        p1 = None
        p2 = node
        
        while p2:
            p3 = p2.next
            p2.next = p1
            p1 = p2
            p2 = p3
            
        
            
        