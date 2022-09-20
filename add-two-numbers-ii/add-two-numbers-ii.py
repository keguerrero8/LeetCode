# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []
        
        p1, p2 = l1, l2
        
        while p1:
            stack1.append(p1.val)
            p1 = p1.next
            
        while p2:
            stack2.append(p2.val)
            p2 = p2.next
        
        head = ListNode(None)
        rem = 0
        
        while stack1 or stack2:
            val1, val2 = 0, 0
            if stack1:
                val1 = stack1.pop()
            if stack2:
                val2 = stack2.pop()

            total = val1 + val2 + rem
            rem = 0
            if total > 9:
                rem = 1
                total = total % 10
                
            temp = head.next
            head.next = ListNode(total)
            head.next.next = temp
            
        if rem != 0:
            temp = head.next
            head.next = ListNode(1)
            head.next.next = temp
            
        return head.next
                
            
        
        