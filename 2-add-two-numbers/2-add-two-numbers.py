# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        sumList = sumListHead = ListNode(None)
        node1, node2 = l1, l2
        rem = 0
        
        while node1 or node2:
            n1Val = node1.val if node1 else 0
            n2Val = node2.val if node2 else 0
            
            res = n1Val + n2Val + rem
            rem = 0
            
            if res > 9:
                res -= 10
                rem = 1
            
            sumList.next = ListNode(res)
            sumList = sumList.next
            
            node1 = node1.next if node1 else node1
            node2 = node2.next if node2 else node2
            
        if rem > 0:
            sumList.next = ListNode(rem)
            
        return sumListHead.next
            
        
        
        